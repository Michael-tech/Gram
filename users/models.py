"""Users Models."""

# Django
from django.contrib.auth.models import AbstractUser
# validations
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Models
from utils.utilmodel import UtilModel


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Profiles(UtilModel):
    """Profile model.
    UtilModel add:  is_active, created, modified
    """

    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    picture = models.ImageField(
        _("Foto"),
        upload_to='static/images/profile/photos',
        default='static/images/default.jpg',
        blank=True,
        null=True
    )

    biography = models.CharField(_("Biografia"), max_length=50)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    
