from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Cook
from ..customers.models import Customer
from ..dishes.models import Dish, DishType, Ingredient


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("years_of_experience",)}),
    )
    list_display = UserAdmin.list_display + ("years_of_experience",)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("years_of_experience", "email")}),
    )


class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff()


admin.site.register(Dish)
admin.site.register(Customer)
admin.site.register(DishType)
admin.site.register(Ingredient)