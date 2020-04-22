"""Models Admin Gram."""

from django.contrib import admin
from django.utils.html import format_html

from gram.models import Notes


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    """Notes admin."""

    list_display = ('pk','user', 'description', 'day','hour',)
    list_display_links = ('pk',)
    list_editable = ('description',)

    search_fields = (
        'user__username',
        'description'
    )

    list_filter = (
        'is_active',
        'created',
        'modified',
    )
