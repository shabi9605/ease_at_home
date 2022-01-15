from django import forms
from django.db.models import fields
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields = ('amount',)
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.helper=FormHelper(self)
    #     self.helper.layout=Layout(
    #         'name',
    #         'amount',
    #         Submit('submit','Pay_Now',css_class='button white btn-block btn-primary')
    #     )
