from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse

from product.views import product
from .models import *
from cart1.models import Cart
from account.models import *
from .forms import *
from django.contrib import messages

# Create your views here.


def order_save(request):
    address=request.POST.get('address')
    address_second=request.POST.get('address_secound')
    postal_code = request.POST.get('zip')
    country = request.POST.get('country')
    state = request.POST.get('state')
    
   
    order = Order.objects.create(user=request.user,address=address,
    address_second=address_second,
    postal_code=postal_code,country=country,state=state,
    
    )   
    cart = Cart.objects.get(user=request.user)
    order.save()
    request.session['order']=order.id
    for item in cart.items.all():
        orderItem, created = OrderItem.objects.update_or_create(user=order.user,
            order=order, product=item.product, price=item.price, quantity=item.quantity)
        order.order_items.add(orderItem)
    return render(request,'payment/process.html')

def order_create(request):
    profile = get_object_or_404(Customer,user=request.user)
    cart = Cart.objects.get(user=request.user)
    return render(request, 'orders/order_list.html', {'cart': cart, 'profile': profile})

def orderview(request):
    order=Order.objects.all()
    return render(request,'order/order_view.html',{'order':order})

def orderitemview(request):
    order=OrderItem.objects.all()
    return render(request,'order/orderitem_view.html',{'order':order})

def neworder(request):
    a=OrderItem.objects.filter(user=request.user)
    return render(request,'orders/neworder.html',{'order':a})

def update_order(request,id):
    Update = OrderItem.objects.get(id=id)
    print(Update)
    form= OrderFormUpdate(instance=Update)
    if request.method=='POST':
        form= OrderFormUpdate(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'order/order_edit.html',{'form':form,'product':Update})

def delete_order(request,id):
    deleteemp = Order.objects.get(id=id)
    deleteemp.delete()
    messages.success(request,'Record deleted succefully')
    return redirect('dashboard/dashboard')



def view_orders(request):
    try:
        print(request.user.volunteer.shop)
        our_orders=OrderItem.objects.filter(seller=request.user.volunteer.shop)
        print(our_orders)
    except:
        our_orders=OrderItem.objects.filter(seller=request.user.shop)

    return render(request,'orders/our_orders.html',{'our_orders':our_orders})

