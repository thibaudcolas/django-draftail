from django.urls import reverse
from django.views import generic

from .forms import FeedbackForm


class DemoFormView(generic.FormView):
    form_class = FeedbackForm
    template_name = "feedback/feedback_form.html"

    def get_success_url(self):
        return reverse("feedback-form")
