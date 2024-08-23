import json
from datetime import datetime

from django.core.management.base import BaseCommand
from django.db.models import Max
from logs.models import NginxLogEntry


class Command(BaseCommand):
    help = "Parse and import Nginx logs from a text file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the log text file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        # Get the last log entry in the database by time
        last_entry_time = NginxLogEntry.objects.aggregate(Max("time"))["time__max"]

        bulk_create_list = []
        batch_size = 100  # Batch size for bulk_create

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Check if the line is not empty
                    log_entry = json.loads(line)

                    # Parse the log entry time
                    log_time = datetime.strptime(
                        log_entry["time"], "%d/%b/%Y:%H:%M:%S %z"
                    )

                    # Skip entries if their time is less than or equal to the time of the last entry in the database
                    if last_entry_time and log_time <= last_entry_time:
                        # Check if this entry already exists in the database
                        exists = NginxLogEntry.objects.filter(
                            remote_ip=log_entry["remote_ip"],
                            time=log_time,
                            http_method=log_entry["request"].split()[0],
                            uri=log_entry["request"].split()[1],
                            response_code=log_entry["response"],
                            response_size=log_entry["bytes"],
                            user_agent=log_entry.get("agent", None),
                            referrer=log_entry.get("referrer", None),
                        ).exists()

                        # If the entry exists, skip it
                        if exists:
                            continue

                    # Add the entry to the list for bulk_create
                    bulk_create_list.append(
                        NginxLogEntry(
                            remote_ip=log_entry["remote_ip"],
                            time=log_time,
                            http_method=log_entry["request"].split()[0],
                            uri=log_entry["request"].split()[1],
                            response_code=log_entry["response"],
                            response_size=log_entry["bytes"],
                            user_agent=log_entry.get("agent", None),
                            referrer=log_entry.get("referrer", None),
                        )
                    )

                    # If the list size reaches batch_size, insert the entries into the database
                    if len(bulk_create_list) >= batch_size:
                        NginxLogEntry.objects.bulk_create(bulk_create_list)
                        bulk_create_list = []

        # Insert the remaining entries
        if bulk_create_list:
            NginxLogEntry.objects.bulk_create(bulk_create_list)

        self.stdout.write(self.style.SUCCESS("Successfully imported log file"))
