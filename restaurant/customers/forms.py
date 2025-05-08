from django.contrib.auth.forms import UserCreationForm, forms

from models import Customer


class CustomerForm(UserCreationForm):
    MIN_BIRTH_YEAR = 1900
    MAX_BIRTH_YEAR = 2025

    class Meta:
        model = Customer
        fields = UserCreationForm.Meta.fields


class DishNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)




