from django.urls import reverse_lazy
from django.views import generic

from restaurant.customers.forms import CustomerForm
from restaurant.customers.models import Customer

class CustomerListView(generic.ListView):
    model = Customer


class CustomerCreateView(generic.CreateView):
   model = Customer
   form_class = CustomerForm
   template_name = "customer_form.html"
   success_url = reverse_lazy("customers:customer-list")


