"""Profile View ."""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView

from users.models import Profiles


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = Profiles
    fields = ["name","picture","biography","phone_number","website"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return Profiles.objects.get(user=self.request.user)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


profile_update_view = ProfileUpdateView.as_view()

