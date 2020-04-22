"""Contact View."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from django.contrib.auth.decorators import login_required
# Models

from gram.models import Contacts


class ContactListView(LoginRequiredMixin, ListView):

    model = Contacts

    def get_queryset(self):

        return Contacts.objects.filter(user=self.request.user)


contact_list_view = ContactListView.as_view()

class ContactCreateView(LoginRequiredMixin, CreateView):

    model = Contacts
    fields = ["name","photo","phone_number","email"]

    def get_success_url(self):
        return reverse("gram:ContactList")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


contact_create_view = ContactCreateView.as_view()

class ContactUpdateView(LoginRequiredMixin, UpdateView):

    model = Contacts
    fields = ["name","photo","phone_number","email"]

    def get_success_url(self):
        return reverse("gram:ContactList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


contact_update_view = ContactUpdateView.as_view()


class ContactDeleteView(LoginRequiredMixin, DeleteView):

    model = Contacts
    template_name = "gram/gram_comfirm_delete.html"

    def get_success_url(self):
        return reverse("gram:ContactList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully Delete")
        )
        return super().form_valid(form)


contact_delete_view = ContactDeleteView.as_view()


