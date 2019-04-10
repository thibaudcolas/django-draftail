from __future__ import absolute_import, unicode_literals

from django.urls import reverse
from django.views import generic

from .forms import DemoForm


class DemoFormView(generic.FormView):
    form_class = DemoForm
    template_name = "demo-form.html"

    def get_success_url(self):
        return reverse("demo-form")


demo_form_view = DemoFormView.as_view()
