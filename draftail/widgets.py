import json
import logging

from django import forms

from .draft_text import DraftText


class DraftailEditor(forms.HiddenInput):
    template_name = "draftail/draftail_editor.html"

    # Do not mark the field as hidden, even though it inherits from a hidden input.
    is_hidden = False

    def __init__(self, *args, **kwargs):
        default_attrs = {"data-django-draftail": "DraftailEditor"}

        attrs = kwargs.get("attrs")
        if attrs:
            default_attrs.update(attrs)
        kwargs["attrs"] = default_attrs

        super(DraftailEditor, self).__init__(*args, **kwargs)

    def render(self, name, value=None, attrs=None, renderer=None):
        json_value = value

        if json_value is None or json_value == "":
            value = None
        else:
            if isinstance(json_value, DraftText):
                json_value = json_value.get_json()
            try:
                value = json.loads(json_value)
            except (ValueError, TypeError):
                value = {}
                logging.getLogger(__name__).warn(
                    "Cannot handle {} as JSON".format(json_value)
                )

        encoded_value = json.dumps(value)

        parent = super(DraftailEditor, self)

        return parent.render(name, encoded_value, attrs, renderer)

    def value_from_datadict(self, data, files, name):
        json_value = super(DraftailEditor, self).value_from_datadict(
            data, files, name
        )

        if json_value is None:
            return None
        elif json_value == "":
            value = {}
        else:
            if isinstance(json_value, DraftText):
                json_value = json_value.get_json()
            try:
                value = json.loads(json_value)
            except (ValueError, TypeError):
                value = {}
                logging.getLogger(__name__).warning(
                    "Cannot handle {} as JSON".format(json_value)
                )

        return json.dumps(value)

    class Media:
        js = ["draftail.bundle.js"]
        css = {"all": ["draftail.bundle.css"]}
