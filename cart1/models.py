from django.db import models
from product.models import Product
from account.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # paid = models.BooleanField(default=False)
    total_amount=models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'cart {}'.format(self.user)

    def get_total_cost(self):
        a=sum(item.get_cost() for item in self.items.all())
        print(a)
        self.total_amount=a
        print(self.total_amount)
        
        return a

    def save(self,*args,**kwargs):
        a=sum(item.get_cost() for item in self.items.all())
        print(a)
        self.total_amount=a
        print(self.total_amount)
        super().save(*args, **kwargs)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',
    null=True,
    on_delete=models.CASCADE,
    )
    product = models.ForeignKey(Product,
    related_name='cart_items',
    on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.product)

    def get_cost(self):
        return self.price * self.quantity

 

