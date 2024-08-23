from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Nginx Log API",
        default_version="v1",
        description="API for Nginx log entries. For authorization use login: admin and pass: admin.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# View for the main page (I didn't create a separate application)
def index(request):
    return render(request, "index.html")


urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/", include("logs.urls")),
]

admin.site.site_header = "Logs - Admin Panel"
admin.site.site_title = "Logs Admin"
admin.site.index_title = "Welcome to the Admin Interface!"
