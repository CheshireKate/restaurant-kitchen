from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
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
   context_object_name = "dish_detail"
   template_name = "dishes/dish_detail.html"

class DishDeleteView(generic.DeleteView, LoginRequiredMixin, IsAdminMixin):
    model = Dish
    context_object_name = "dish_confirm_delete"
    template_name = "dishes/dish_detail.html"


class DishCreateView(generic.CreateView, LoginRequiredMixin, IsAdminMixin):
    model = Dish
    context_object_name = "dish_create"
    template_name = "dishes/dish_detail.html"


class DishUpdateView(generic.UpdateView, LoginRequiredMixin, IsAdminMixin):
    model = Dish
    context_object_name = "dish_update"
    template_name = "dishes/dish_detail.html"

