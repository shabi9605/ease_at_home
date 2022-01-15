from django import forms
from django.db.models import fields
from django.forms.fields import DateField
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2','email')
        labels=('password1','password','password2','confirm password')



class ShopRegisterForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields=('shop_name','phone','license_no','location','proof','category')


class HomeServicerRegisterForm(forms.ModelForm):
    class Meta:
        model=HomeServicer
        fields=('phone','location','proof','qualification','category')



class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('phone','location')



class VolunteerRegisterForm(forms.ModelForm):
    class Meta:
        model=Volunteer
        fields=('phone','qualification','location','id_proof')



class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    
    class Meta:
        model=User
        fields=('username',)

class UpdateProfileForm(forms.ModelForm):
    address=forms.Textarea()
    
    class Meta:
        model=Volunteer
        fields=('phone','qualification','location','id_proof')


class VolunteerAvailabilityForm(forms.ModelForm):
    available='available'
    not_available='not_available'
    availability_statuses=[
        (available,'available'),
        (not_available,'not_available')
    ]
    availability_status=forms.ChoiceField(choices=availability_statuses,required=True)
    
    class Meta:
        model=Volunteer
        fields=('availability_status',)


class ServicerAvailabilityForm(forms.ModelForm):
    available='available'
    not_available='not_available'
    availability_statuses=[
        (available,'available'),
        (not_available,'not_available')
    ]
    availability_status=forms.ChoiceField(choices=availability_statuses,required=True)
    
    class Meta:
        model=HomeServicer
        fields=('availability_status',)



class BookingForm(forms.ModelForm):
    wanted_date=DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Booking
        fields=('wanted_date','place')

class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=('status','paid_status','amount')





