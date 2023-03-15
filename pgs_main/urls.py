from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("pgs_admin/", admin.site.urls),
    path("", include("core.urls")),
]
