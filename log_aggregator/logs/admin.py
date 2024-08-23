from django.contrib import admin

from logs.models import NginxLogEntry


@admin.register(NginxLogEntry)
class NginxLogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "time",
        "remote_ip",
        "http_method",
        "uri",
        "response_code",
        "response_size",
    )
    search_fields = ("remote_ip", "uri", "user_agent")
    list_filter = ("response_code", "http_method", "time")
