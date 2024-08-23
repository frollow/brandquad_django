from django.urls import include, path
from rest_framework.routers import DefaultRouter

from logs.views import NginxLogEntryViewSet

router = DefaultRouter()
router.register(r"logs", NginxLogEntryViewSet)


urlpatterns = [
    path("", include(router.urls), name="api-root"),
]
