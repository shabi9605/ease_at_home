from re import T
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django.utils import timezone

# Create your models here.

class ShopCategory(models.Model):
    category_name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.category_name)


class HomeServicerCategory(models.Model):
    servicer_category_name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.servicer_category_name)


class Shop(models.Model):
    shop_name=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=PhoneNumberField()
    license_no=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    proof=models.FileField(upload_to='proof',null=True,blank=True)
    category=models.ForeignKey(ShopCategory,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.shop_name)


class HomeServicer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=PhoneNumberField()
    location=models.CharField(max_length=50)
    proof=models.FileField(upload_to='proof',null=True,blank=True)
    qualification=models.CharField(max_length=50)
    category=models.ForeignKey(HomeServicerCategory,on_delete=models.CASCADE,null=True,blank=True)
    available='available'
    not_available='not_available'
    availability_statuses=[
        (available,'available'),
        (not_available,'not_available')
    ]
    availability_status=models.CharField(max_length=50,choices=availability_statuses,default=available)
    def __str__(self):
        return str(self.user.username)


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=PhoneNumberField()
    location=models.CharField(max_length=50)
    def __str__(self):
        return str(self.user.username)



class Volunteer(models.Model):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=PhoneNumberField()
    qualification=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    available='available'
    not_available='not_available'
    availability_statuses=[
        (available,'available'),
        (not_available,'not_available')
    ]
    availability_status=models.CharField(max_length=50,choices=availability_statuses,default=available)
    id_proof=models.FileField(upload_to='proof',null=True,blank=True)
    def __str__(self):
        return str(self.user.username)



class Booking(models.Model):
    servicer=models.ForeignKey(HomeServicer,on_delete=models.CASCADE,null=True,blank=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateTimeField(default=timezone.now)
    wanted_date=models.DateField()
    place=models.CharField(max_length=50)
    accepted='accepted'
    rejected='rejected'
    pending='pending'
    statuses=[
        (accepted,'accepted'),
        (rejected,'rejected'),
        (pending,'pending')
    ]
    status=models.CharField(max_length=50,choices=statuses,default=pending)
    paid='paid'
    notpaid='notpaid'
    paid_statuses=[
        (paid,'paid'),
        (notpaid,'notpaid')
    ]
    paid_status=models.CharField(max_length=30,choices=paid_statuses,default=notpaid)
    amount=models.IntegerField(default=400)
    def __str__(self):
        return str(self.customer.user.username)



