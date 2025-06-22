from django.urls import path, include

from restaurant.cooks.views import test_session_view, CookListView, CookDetailView, CookDeleteView, CookUpdateView

urlpatterns = [
    path("", CookListView.as_view(), name="cooks_list"),
    path("<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
    path("<int:pk>/update", CookUpdateView.as_view(), name="cook_update"),
    path("<int:pk>/delete", CookDeleteView.as_view(), name="cook_delete"),
    path("test-session/", test_session_view, name="test-session"),
]


app_name="cooks"