from django.urls import path

from . import views

app_name = "feedback"
urlpatterns = [
    path("form/", views.DemoFormView.as_view(), name="feedback-form")
]
