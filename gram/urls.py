from django.urls import path

from .views import (contact_create_view, contact_delete_view,
                    contact_list_view, contact_update_view,
                    my_product_list_view, note_create_view, note_delete_view,
                    note_list_view, note_update_view, post_create_view,
                    post_delete_view, post_list_view, post_update_view,
                    product_create_view, product_delete_view,
                    product_list_view, product_update_view)

app_name = "gram"
urlpatterns = [
    # Post
    path("posts/", view=post_list_view, name="PostList"),
    path("posts/create/", view=post_create_view, name="PostCreate"),
    path("posts/update/<pk>", view=post_update_view, name="PostUpdate"),
    path("posts/delete/<pk>", view=post_delete_view, name="PostDelete"),
    # Notes
    path("notes/", view=note_list_view, name="NoteList"),
    path("notes/create/", view=note_create_view, name="NoteCreate"),
    path("notes/update/<pk>", view=note_update_view, name="NoteUpdate"),
    path("notes/delete/<pk>", view=note_delete_view, name="NoteDelete"),

    # Contacts
    path("contacts/", view=contact_list_view, name="ContactList"),
    path("contacts/create/", view=contact_create_view, name="ContactCreate"),
    path("contacts/update/<pk>", view=contact_update_view, name="ContactUpdate"),
    path("contacts/delete/<pk>", view=contact_delete_view, name="ContactDelete"),

    # Products
    path("shop/", view=product_list_view, name="ProductList"),
    path("products/", view=my_product_list_view, name="MyProductList"),
    path("products/create/", view=product_create_view, name="ProductCreate"),
    path("products/update/<pk>", view=product_update_view, name="ProductUpdate"),
    path("products/delete/<pk>", view=product_delete_view, name="ProductDelete"),


]
