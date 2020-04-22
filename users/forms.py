from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from users.models import Profiles


class SignupForm(forms.Form):

    def signup(self, request, user):

        user.save()
        profile = Profiles(user=user)
        profile.save()
