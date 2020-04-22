"""Models Admin Gram."""

from django.contrib import admin
from django.utils.html import format_html

from gram.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Contactos admin."""

    list_display = ('pk', 'name', 'phone_number', 'email',)
    list_display_links = ('pk','name',)
    list_editable = ('phone_number', 'email',)

    search_fields = (
        'user__username',
        'name',
        'phone_number'
    )

    list_filter = (
        'is_active',
        'created',
        'modified',
    )

