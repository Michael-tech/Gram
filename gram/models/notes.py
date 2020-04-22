"""Notes models."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Models
from utils.utilmodel import UtilModel


class Notes(UtilModel):
    """Notes model."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    description = models.CharField(_("Descripcion"),max_length=255)
    day = models.CharField(_("Dia"), max_length=50)
    hour = models.CharField(_("Hora"), max_length=50)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.description, self.user.username)
