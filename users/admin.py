from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from .models import Profiles

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    list_display = ["username", "is_superuser"]
    search_fields = ["username"]


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'name', 'phone_number', 'website',)
    list_display_links = ('pk', 'name',)
    list_editable = ('phone_number', 'website',)

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user','name', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profiles
    can_delete = False
    verbose_name_plural = 'profiles'
