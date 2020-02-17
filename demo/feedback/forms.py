from django import forms
from django.forms import CharField


class FeedbackForm(forms.Form):
    message = CharField()
