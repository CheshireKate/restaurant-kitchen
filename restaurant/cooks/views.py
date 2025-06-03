from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from restaurant.cooks.admin import IsAdminMixin
from restaurant.cooks.models import Cook
from restaurant.dishes.models import Dish

def is_admin(user):
    return user.is_staff

def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_visits": num_visits + 1,
    }

    return render(request, "index.html", context=context)


class CookListView(generic.ListView, LoginRequiredMixin, IsAdminMixin):
   model = Cook
   context_object_name = "cooks_list"
   template_name = "cooks_list.html"


class CookDetailView(generic.DetailView):
    model = Cook
    context_object_name = "cook_detail"
    template_name = "cook_detail.html"


class CookDeleteView(generic.DeleteView, LoginRequiredMixin, IsAdminMixin):
    model = Cook
    context_object_name = "cook_delete"
    template_name = "cook_confirm_delete.html"
    success_url = reverse_lazy("cooks:cooks_list")


class CookUpdateView(generic.UpdateView, LoginRequiredMixin, IsAdminMixin):
    model = Cook
    context_object_name = "cook_update"
    template_name = "cook_update.html"
    success_url = reverse_lazy("cooks:cooks_detail")


def test_session_view(request):
    request.session["test"] = "test session"
    return HttpResponse(
        f"<h1>Session data: {request.session['test']}</h1>"
    )




