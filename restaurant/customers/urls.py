from django.urls import path

from restaurant.customers.views import CustomerCreateView, CustomerListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list"),
    path("customers/create/", CustomerCreateView.as_view(), name="customer_create"),
]
