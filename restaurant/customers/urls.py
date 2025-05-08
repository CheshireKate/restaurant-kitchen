from django.urls import path

from restaurant.customers.views import CustomerCreateView, CustomerListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path("customers/create/", CustomerCreateView.as_view(), name="customer-create"),
]
