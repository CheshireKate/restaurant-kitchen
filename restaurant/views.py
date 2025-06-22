from django.db.models import Q
from django.shortcuts import render
from restaurant.cooks.models import Cook
from restaurant.dishes.models import Dish
from restaurant.forms import SearchForm


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
    return render(request, "main.html", context=context)


def search_view(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            cooks = Cook.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
            dishes = Dish.objects.filter(name__icontains=query)
            results.extend(cooks)
            results.extend(dishes)
    return render(request, 'search.html', {
        'search_form': form,
        'results': results,
    })