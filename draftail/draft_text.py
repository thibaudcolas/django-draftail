# import json

from django.conf import settings
from django.utils.functional import cached_property
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from draftjs_exporter.defaults import BLOCK_MAP, STYLE_MAP

# from draftjs_exporter.html import HTML

_exporter_config = None


def get_exporter_config():
    """
    https://github.com/springload/wagtaildraftail/blob/87f1ae3ade493c00daff021394051aa656136c10/wagtaildraftail/utils.py#L12
    """
    global _exporter_config

    if not _exporter_config:
        # Get from settings.
        entity_decorators = getattr(
            settings, "DRAFT_EXPORTER_ENTITY_DECORATORS", {}
        )
        composite_decorators = getattr(
            settings, "DRAFT_EXPORTER_COMPOSITE_DECORATORS", []
        )
        block_map = getattr(settings, "DRAFT_EXPORTER_BLOCK_MAP", BLOCK_MAP)
        style_map = getattr(settings, "DRAFT_EXPORTER_STYLE_MAP", STYLE_MAP)

        # Load classes.
        for entity_id, decorator in entity_decorators.items():
            entity_decorators[entity_id] = import_string(decorator)

        # Save
        _exporter_config = {
            "entity_decorators": entity_decorators,
            "composite_decorators": [
                import_string(decorator) for decorator in composite_decorators
            ],
            "block_map": block_map,
            "style_map": style_map,
        }

    return _exporter_config


class DraftText:
    """
    A custom object used to represent a renderable rich text value.
    Provides a 'source' property to access the original source code,
    and renders to the front-end HTML rendering.
    Original Wagtail implementation(s):
    - https://github.com/springload/wagtaildraftail/blob/87f1ae3ade493c00daff021394051aa656136c10/wagtaildraftail/draft_text.py#L14
    - https://github.com/wagtail/wagtail/blob/4b35053a92c60545a8f02668e3f2d7376f28a18d/wagtail/core/rich_text/__init__.py#L33
    """

    def __init__(self, source, **kwargs):
        # self.exporter = HTML(get_exporter_config())
        self.source = source or ""

    def get_json(self):
        return self.source

    @cached_property
    def _html(self):
        pass
        # return self.exporter.render(json.loads(self.source))

    def __html__(self):
        return self._html

    def __str__(self):
        return mark_safe(self.__html__())

    def __eq__(self, other):
        return (
            hasattr(other, "__html__") and self.__html__() == other.__html__()
        )

    def __bool__(self):
        return bool(self.source)

    __nonzero__ = __bool__
