from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Permissions', {'fields': ('is_staff', 'groups', 'user_permissions')}),
    )
    list_display = UserAdmin.list_display + ('is_staff',)