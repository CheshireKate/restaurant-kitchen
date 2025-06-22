from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from restaurant.cooks.admin import IsAdminMixin
from restaurant.dishes.models import Dish

def is_admin(user):
    return user.is_staff


class DishListView(generic.ListView):
   model = Dish
   context_object_name = "dishes_list"
   template_name = "dishes/dishes_list.html"
   paginate_by = 5


class DishDetailView(generic.DetailView):
   model = Dish
   context_object_name = "dish"
   template_name = "dishes/dish_detail.html"


class DishDeleteView(LoginRequiredMixin, IsAdminMixin, generic.DeleteView):
    model = Dish
    context_object_name = "dish"
    template_name = "dishes/dish_confirm_delete.html"
    success_url = reverse_lazy("dishes:dishes_list")


class DishCreateView(LoginRequiredMixin, IsAdminMixin, generic.CreateView):
    model = Dish
    context_object_name = "dish"
    template_name = "dishes/dish_detail.html"


class DishUpdateView(LoginRequiredMixin, IsAdminMixin, generic.UpdateView):
    model = Dish
    context_object_name = "dish"
    template_name = "dishes/dish_update.html"
    fields = ["name", "description", "price", "dish_type", "cooks", "ingredients"]

    def get_success_url(self):
        return reverse_lazy("dishes:dish_detail", kwargs={"pk": self.object.pk})

