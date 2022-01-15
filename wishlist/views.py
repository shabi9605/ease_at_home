from django.shortcuts import render

from django.shortcuts import render, redirect, 	get_object_or_404
from product.models import Product
from django.contrib.auth.decorators import login_required
from .models import Wishlist, WishlistItem
from account.models import *
# Create your views here.


@login_required
def wishlist_add(request, product_id,):

    obj, created = Wishlist.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = WishlistItem.objects.update_or_create(wishlist=obj, product=product)
    obj.wishlist_items.add(item)
    item.save()
    obj.save()
    return redirect('wishlist:wishlist_detail')




def wishlist_remove(request, product_id):
    obj, created = Wishlist.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    wishlistItems = WishlistItem.objects.filter(wishlist=obj, product=product)
    wishlistItems.delete()
    return redirect('wishlist:wishlist_detail')


@login_required
def wishlist_detail(request):
    wishlist = Wishlist.objects.get(user=request.user)
    return render(request, 'wishlist/wishlist_detail.html', {'wishlist': wishlist})
