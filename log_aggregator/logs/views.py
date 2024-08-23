from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import NginxLogEntry
from .serializers import NginxLogEntrySerializer


class NginxLogEntryViewSet(viewsets.ModelViewSet):
    queryset = NginxLogEntry.objects.all()
    serializer_class = NginxLogEntrySerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["remote_ip", "response_code", "http_method"]
    search_fields = ["uri", "user_agent"]
    ordering_fields = ["time", "response_size"]
