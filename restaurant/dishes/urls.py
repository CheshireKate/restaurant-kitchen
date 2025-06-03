from django.urls import include, path

from .views import DishListView, DishDetailView, DishUpdateView, DishDeleteView

urlpatterns = [
    path("restaurant/dishes/", DishListView, namespace="dishes=list"),
    path("restaurant/dishes/<int:pk>/", DishDetailView.as_view(), name="cook-detail"),
    path("restaurant/dishes/<int:pk>/update", DishUpdateView.as_view(), name="cook-update"),
    path("restaurant/dishes/<int:pk>/delete", DishDeleteView.as_view(), name="cook-delete"),
]


app_name="dishes"