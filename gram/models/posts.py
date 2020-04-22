"""Posts models."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Models
from utils.utilmodel import UtilModel


class Posts(UtilModel):
    """Post model."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to='static/images/posts/photos',
        blank=False,
        null=False
    )

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)
