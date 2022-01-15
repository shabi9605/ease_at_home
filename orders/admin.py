from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(OrderItem)
class Adminorder(admin.ModelAdmin):
    list_display=['user','address','postal_code','country','state','created','updated']
    
admin.site.register(Order,Adminorder)