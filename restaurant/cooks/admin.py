from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook


@admin.register(Cook)
class DriverAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets