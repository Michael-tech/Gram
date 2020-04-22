"""Post View."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from django.contrib.auth.decorators import login_required
# Models

from gram.models import Posts


class PostListView(LoginRequiredMixin, ListView):

    model = Posts

    def get_queryset(self):

        return Posts.objects.filter(user=self.request.user)


post_list_view = PostListView.as_view()

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Posts
    fields = ["title","photo"]

    def get_success_url(self):
        return reverse("gram:PostList")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


post_create_view = PostCreateView.as_view()

class PostUpdateView(LoginRequiredMixin, UpdateView):

    model = Posts
    fields = ["title","photo"]

    def get_success_url(self):
        return reverse("gram:PostList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


post_update_view = PostUpdateView.as_view()


class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Posts
    template_name = "gram/gram_comfirm_delete.html"

    def get_success_url(self):
        return reverse("gram:PostList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully Delete")
        )
        return super().form_valid(form)


post_delete_view = PostDeleteView.as_view()


