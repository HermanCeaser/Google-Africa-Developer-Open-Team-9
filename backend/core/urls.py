from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("complaint.urls", namespace="complaint")),
    path("api/", include("complaint_api.urls", namespace="complaint_api")),
    path("api/account/", include("account.api.urls", namespace="account_api")),
    path("account/", include("django.contrib.auth.urls")),
]
