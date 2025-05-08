from multiprocessing.dummy.connection import Client

from django.contrib.auth import get_user_model
from django.db.models import Model
from django.db.models.fields import json
from django.test import TestCase
from django.urls import reverse

from restaurant.cooks.models import Cook
from restaurant.customers.forms import CustomerForm
from restaurant.dishes.models import DishType, Dish, Ingredient


class ModelTest(TestCase):
	def test_model(self):
		obj = Model.objects.create()
		self.asserEqual(str(obj), obj)


class AdminPanelTest(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.client.force_login(self.admin_user)

    def test_list_display(self):
        url = reverse("admin:post_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.post.title)


class ViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_view_list(self) -> None:
        url = reverse("cooks:list")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_update_dish_type(self):
        self.dish = Dish.objects.create(name="Borsch",
                                        price=50.5,
                                        dish_type=DishType.objects.create(name="soup"),
                                        cooks=Cook.objects.create(first_name="Ivan", last_name="Petrov"),
                                        ingredients=Ingredient.objects.create(name="beetroot")
                                        ),
        url = reverse("dish:detail", args=[self.dish.id])

        res = self.client.patch(
            url,
            content_type="application/json",
            data=json.dumps(
                {"name": "New name"}
            )
        )
        self.assertEqual(self.dish.name, "New title")

class FormTest(TestCase):

    def test_form_is_valid(self):
        form_data = {
            "full_name": "Marua",
            "birth_year": 1989
        }
        form = CustomerForm(data=form_data)
        self.assertEqual(form.is_valid())
