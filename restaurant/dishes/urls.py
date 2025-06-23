from django.urls import include, path

from .views import DishListView, DishDetailView, DishUpdateView, DishDeleteView

urlpatterns = [
    path("", DishListView.as_view(), name="dishes_list"),
    path("<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("<int:pk>/update", DishUpdateView.as_view(), name="dish_update"),
    path("<int:pk>/delete", DishDeleteView.as_view(), name="dish_delete"),
]


app_name="dishes"