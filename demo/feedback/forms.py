from django import forms
from django.forms import CharField
from draftail.fields import DraftailFormField


class FeedbackForm(forms.Form):
    message = CharField()
    rich_message = DraftailFormField()
