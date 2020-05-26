from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("demo.polls.urls")),
    path("feedback/", include("demo.feedback.urls")),
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
]
