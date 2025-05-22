from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets
    list_display = UserAdmin.list_display


class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff()