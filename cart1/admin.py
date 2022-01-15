

from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Cart)


class AdminCartItem(admin.ModelAdmin):
    list_display=['cart','product','price','quantity']
   
    

admin.site.register(CartItem,AdminCartItem)