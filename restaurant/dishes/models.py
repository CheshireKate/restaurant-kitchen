from django.db import models
from django.urls import reverse

from restaurant.cooks.models import Cook


class DishType(models.Model):
    name = models.CharField(max_length=250, primary_key=True, db_index=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=250, primary_key=True, db_index=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=250, primary_key=True, db_index=True)
    description = models.CharField(max_length=500, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)
    ingredients = models.ManyToManyField(Ingredient)

    def get_absolute_url(self):
        return reverse("dishes:dish-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Dishes"