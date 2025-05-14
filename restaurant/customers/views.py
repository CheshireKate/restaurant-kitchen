from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from restaurant.cooks.views import is_admin
from restaurant.customers.forms import CustomerForm
from restaurant.customers.models import Customer

@method_decorator([login_required, user_passes_test(is_admin)], name='dispatch')
class CustomerListView(generic.ListView):
    model = Customer


class CustomerCreateView(generic.CreateView):
   model = Customer
   form_class = CustomerForm
   template_name = "customer_form.html"
   success_url = reverse_lazy("customers:customer-list")


