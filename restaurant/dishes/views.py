from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import generic

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

@login_required
@user_passes_test(is_admin)
class DishDeleteView(generic.DeleteView):
    model = Dish
    context_object_name = "dish_confirm_delete"
    template_name = "dishes/dish_detail.html"

@login_required
@user_passes_test(is_admin)
class DishCreateView(generic.CreateView):
    model = Dish
    context_object_name = "dish_create"
    template_name = "dishes/dish_detail.html"

@login_required
@user_passes_test(is_admin)
class DishUpdateView(generic.UpdateView):
    model = Dish
    context_object_name = "dish_update"
    template_name = "dishes/dish_detail.html"

