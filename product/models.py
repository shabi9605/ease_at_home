from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from account.models import *



   
class Product(models.Model):
    
    name=models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image=models.ImageField(upload_to='product_image/%Y/%m/%d')
    price=models.PositiveIntegerField()
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,null=True,blank=True)
    location=models.CharField(max_length=50)
    category=models.ForeignKey(ShopCategory,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('account:product_detail', args=[self.id, self.slug])


    