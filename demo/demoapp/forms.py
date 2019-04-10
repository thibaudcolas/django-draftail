from __future__ import absolute_import, unicode_literals

from django import forms
from django.forms import CharField


# from ckeditor.fields import RichTextFormField


class DemoForm(forms.Form):
    content = CharField()
