
from django.db import models
from cart1.models import *
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    # name=models.CharField(max_length=20)
    amount = models.CharField(max_length=100)
    payment_id=models.CharField(max_length=200,blank=True)
    order_id=models.CharField(max_length=20,blank=True)
    is_paid=models.BooleanField(default=False)
    # cart=models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True)
    total_amount=models.PositiveIntegerField(default=0)
    all_total=models.PositiveIntegerField(default=0)
    date=models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return str(self.user)

    def save(self,*args,**kwargs):
        if self.is_paid == True:
            self.all_total=self.all_total+int(self.total_amount)
            print(self.all_total)
        super().save(*args, **kwargs)