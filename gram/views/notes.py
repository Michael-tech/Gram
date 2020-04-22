"""Post View."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, CreateView, DeleteView

from django.contrib.auth.decorators import login_required
# Models

from gram.models import Notes


class NotesListView(LoginRequiredMixin, ListView):

    model = Notes

    def get_object(self):
        return Notes.objects.filter(user=self.request.user)


note_list_view = NotesListView.as_view()

class NoteCreateView(LoginRequiredMixin, CreateView):

    model = Notes
    fields = ["description","day","hour"]

    def get_success_url(self):
        return reverse("gram:NoteList")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


note_create_view = NoteCreateView.as_view()

class NoteUpdateView(LoginRequiredMixin, UpdateView):

    model = Notes
    fields = ["description","day","hour"]

    def get_success_url(self):
        return reverse("gram:NoteList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


note_update_view = NoteUpdateView.as_view()


class NoteDeleteView(LoginRequiredMixin, DeleteView):

    model = Notes
    template_name = "gram/gram_comfirm_delete.html"

    def get_success_url(self):
        return reverse("gram:NoteList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully Delete")
        )
        return super().form_valid(form)


note_delete_view = NoteDeleteView.as_view()
