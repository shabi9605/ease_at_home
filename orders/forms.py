from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('address','address_second','postal_code','country','state')

class OrderFormUpdate(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"

