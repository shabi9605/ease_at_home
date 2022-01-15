from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','image','price','quantity','description','is_available','created']
    \


admin.site.register(Product,ProductAdmin)