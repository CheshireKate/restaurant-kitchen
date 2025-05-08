from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.cooks.models import Cook
from restaurant.dishes.models import Dish


@login_required
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

    return render(request, "restaurant/index.html", context=context)


class CookListView(generic.ListView):
   model = Cook
   context_object_name = "cooks_list"
   template_name = "cooks/cooks_list.html"


class CookDetailView(generic.DetailView):
    model = Cook
    context_object_name = "cook_detail"
    template_name = "cooks/cook_detail.html"


class CookDeleteView(generic.DeleteView):
    model = Cook
    context_object_name = "cook_delete"
    template_name = "cooks/cook_confirm_delete.html"
    success_url = reverse_lazy("cooks:cooks_list")

@login_required()
class CookUpdateView(generic.UpdateView):
    model = Cook
    context_object_name = "cook_update"
    template_name = "cooks/cook_update.html"
    success_url = reverse_lazy("cooks:cooks_detail")


def test_session_view(request):
    request.session["test"] = "test session"
    return HttpResponse(
        f"<h1>Session data: {request.session['test']}</h1>"
    )




