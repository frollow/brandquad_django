from django.db import models


class NginxLogEntry(models.Model):
    remote_ip = models.GenericIPAddressField()
    time = models.DateTimeField()
    http_method = models.CharField(max_length=10)
    uri = models.CharField(max_length=255)
    response_code = models.IntegerField()
    response_size = models.BigIntegerField()
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.time} - {self.remote_ip} - {self.http_method} {self.uri}"

    class Meta:
        indexes = [
            models.Index(fields=["remote_ip"]),
            models.Index(fields=["time"]),
            models.Index(fields=["http_method"]),
            models.Index(fields=["uri"]),
            models.Index(fields=["response_code"]),
        ]
