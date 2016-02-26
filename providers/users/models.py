from __future__ import unicode_literals

import uuid

from django.db import models
from django.conf import global_settings
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from contrib import CURRENCIES


@python_2_unicode_compatible
class User(AbstractUser):
    """
    Provider
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=100)
    phone_number = models.CharField(_("Phone number"), max_length=30)
    language = models.CharField(
        _("Language"), max_length=2, choices=global_settings.LANGUAGES,
        default='en'
    )
    currency = models.CharField(
        _("Currency"), max_length=3, choices=CURRENCIES, default='USD'
    )

    def __str__(self):
        return self.username
