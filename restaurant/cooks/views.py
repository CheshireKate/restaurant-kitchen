from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.cooks.admin import IsAdminMixin
from restaurant.cooks.models import Cook
from restaurant.dishes.models import Dish

def is_admin(user):
    return user.is_staff

class CookListView(generic.ListView):
   model = Cook
   context_object_name = "cooks_list"
   template_name = "cooks/cooks_list.html"


class CookDetailView(generic.DetailView):
    model = Cook
    context_object_name = "cook"
    template_name = "cooks/cook_detail.html"


class CookDeleteView(LoginRequiredMixin, IsAdminMixin, generic.DeleteView):
    model = Cook
    context_object_name = "cook"
    template_name = "cooks/cook_confirm_delete.html"
    success_url = reverse_lazy("cooks:cooks_list")


class CookUpdateView(LoginRequiredMixin, IsAdminMixin, generic.UpdateView):
    model = Cook
    fields = ["first_name", "last_name", "years_of_experience"]
    context_object_name = "cook"
    template_name = "cooks/cook_update.html"

    def get_success_url(self):
        return reverse_lazy("cooks:cook_detail", kwargs={"pk": self.object.pk})


def test_session_view(request):
    request.session["test"] = "test session"
    return HttpResponse(
        f"<h1>Session data: {request.session['test']}</h1>"
    )




