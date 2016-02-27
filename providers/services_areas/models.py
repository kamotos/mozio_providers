import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import User


class ServiceArea(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.ForeignKey(User, verbose_name=_("Provider"))
    name = models.CharField(_("Name"), max_length=255)
    area = models.PolygonField(_("Service area"))
    price = models.DecimalField(
        _("Price"), max_digits=10, decimal_places=2, default=0)

    objects = models.GeoManager()