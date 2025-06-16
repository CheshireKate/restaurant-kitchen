from django.urls import path, include

from restaurant.cooks.views import test_session_view, CookListView, CookDetailView, CookDeleteView, CookUpdateView

urlpatterns = [
    path("", CookListView.as_view(), name="cooks-list"),
    path("<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
    path("test-session/", test_session_view, name="test-session"),
]


app_name="cooks"