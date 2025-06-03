from django.contrib.auth.forms import UserCreationForm, forms

from restaurant.customers.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'birth_year']


class DishNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)




