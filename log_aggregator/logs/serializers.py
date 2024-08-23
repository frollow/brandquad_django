from rest_framework import serializers

from logs.models import NginxLogEntry


class NginxLogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = NginxLogEntry
        fields = "__all__"
