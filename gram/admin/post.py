"""Models Admin Gram."""

from django.contrib import admin
from django.utils.html import format_html

from gram.models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    """Posts admin."""

    list_display = ('pk','user', 'title',)
    list_display_links = ('pk','title', 'user',)

    search_fields = (
        'user__username',
        'description',
        'title',
    )

    list_filter = (
        'is_active',
        'created',
        'modified',
    )


