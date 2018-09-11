from __future__ import unicode_literals

from django.contrib.contenttypes.admin import (  # NOQA isort:skip
    GenericInlineModelAdmin, GenericStackedInline, GenericTabularInline,
)
from django.contrib.contenttypes.fields import (  # NOQA isort:skip
    GenericForeignKey, GenericRelation,
)
from django.contrib.contenttypes.forms import (  # NOQA isort:skip
    BaseGenericInlineFormSet, generic_inlineformset_factory,
)
