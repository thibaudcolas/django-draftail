import json
import logging

from django import forms

from .draft_text import DraftText


class DraftailEditor(forms.HiddenInput):
    def __init__(self, attrs=None, options=None, features=None):
        super(DraftailEditor, self).__init__(attrs)

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

    @property
    def is_hidden(self):
        """Do not mark the field as hidden, even though it inherits from a hidden input."""
        return False

    class Media:
        js = ["draftail/draftail.js"]
        css = {"all": ["draftail/draftail.css"]}
