"""Products models."""

from django.core.validators import RegexValidator
# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Models
from utils.utilmodel import UtilModel


class Products(UtilModel):
    """Products model."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    photo = models.ImageField(
        _("Foto"),
        upload_to='static/images/productos/photos',
        default='static/images/default.jpg',
        blank=True,
        null=True
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    description = models.CharField(_("Descripcion"), max_length=250)
    price = models.DecimalField(_("Precio"), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_("Stock"))

    def __str__(self):
        return self.name
