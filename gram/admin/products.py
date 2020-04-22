"""Models Admin Gram."""

from django.contrib import admin
from django.utils.html import format_html

from gram.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """Products admin."""

    list_display = ('pk', 'name', 'description','price','stock')
    list_display_links = ('pk','name',)
    list_editable = ('price', 'stock',)

    search_fields = (
        'user__username',
        'description',
        'name',
        'price',
    )

    list_filter = (
        'is_active',
        'created',
        'modified',
        'price', 
    )
