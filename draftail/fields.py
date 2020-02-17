from django import forms
from django.db import models
from django.utils.encoding import force_text

from .draft_text import DraftText
from .validators import EMPTY_SERIALIZED_JSON_VALUES
from .widgets import DraftailEditor


class RichTextField(models.TextField):
    empty_values = list(EMPTY_SERIALIZED_JSON_VALUES)

    def __init__(self, *args, **kwargs):
        super(RichTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"form_class": DraftailFormField}
        defaults.update(kwargs)
        return super(RichTextField, self).formfield(**defaults)

    def to_python(self, value):
        if not isinstance(value, DraftText):
            value = DraftText(value)
        return value

    def get_prep_value(self, value):
        if isinstance(value, DraftText):
            value = value.get_json()

        value = super(RichTextField, self).get_prep_value(value)

        # Django>1.8 does `to_python` in get_prep_value
        if isinstance(value, DraftText):
            value = value.get_json()

        return value

    def from_db_value(self, value, *args, **kwargs):
        if not isinstance(value, DraftText):
            value = DraftText(value)
        return value

    def value_to_string(self, obj):
        if obj is not None:
            value = self.value_from_object(obj)
        else:
            value = self.get_default()

        if isinstance(value, DraftText):
            value = value.get_json()

        return value

    def get_searchable_content(self, value):
        if not isinstance(value, DraftText):
            value = DraftText(value)
        return [force_text(value.__html__())]


class DraftailFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({"widget": DraftailEditor()})
        super(DraftailFormField, self).__init__(*args, **kwargs)
