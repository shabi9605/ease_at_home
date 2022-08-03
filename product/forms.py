from django import forms
from django.db.models import fields
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField





class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields = ('name','image','price','quantity','description','category','is_available','created')