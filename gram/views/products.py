"""Product View."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from django.contrib.auth.decorators import login_required
# Models

from gram.models import Products


class ProductListView(ListView):

    model = Products
    template_name = "gram/shop.html"


product_list_view = ProductListView.as_view()


class MyProductListView(LoginRequiredMixin, ListView):

    model = Products

    def get_queryset(self):

        return Products.objects.filter(user=self.request.user)


my_product_list_view = MyProductListView.as_view()

class ProductCreateView(LoginRequiredMixin, CreateView):

    model = Products
    fields = ["name","photo","phone_number","description","price","stock"]

    def get_success_url(self):
        return reverse("gram:ProductList")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


product_create_view = ProductCreateView.as_view()

class ProductUpdateView(LoginRequiredMixin, UpdateView):

    model = Products
    fields = ["name","photo","phone_number","description","price","stock"]

    def get_success_url(self):
        return reverse("gram:ProductList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


product_update_view = ProductUpdateView.as_view()


class ProductDeleteView(LoginRequiredMixin, DeleteView):

    model = Products
    template_name = "gram/gram_comfirm_delete.html"

    def get_success_url(self):
        return reverse("gram:ProductList")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully Delete")
        )
        return super().form_valid(form)


product_delete_view = ProductDeleteView.as_view()


