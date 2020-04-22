"""Contacts models."""

# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# Models
from utils.utilmodel import UtilModel


class Contacts(UtilModel):
    """Contacts model."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    photo = models.ImageField(
        _("Foto"),
        upload_to='static/images/contactos/photos',
        default='static/images/default.jpg',
        blank=True,
        null=True
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    email = models.EmailField(_("Email"), max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name
