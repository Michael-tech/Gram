"""
Django settings Local for gettingstarted project.

"""
from .base import *
import environ

env = environ.Env()


DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ncMw/4F1iXxb8433XpCJOrUh8cwu250D6OsnWD0LF1uECWwjRlivrzG3BH027qT5SdP7A77Jp30cCCO9FAeFAA=="


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)


