import re
from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.auth.decorators import login_required


# Create your views here.






# create Product
def product_create(request):
    shop=Shop.objects.get(user=request.user)
    print(shop.location)
    if request.method=='POST':
        shop=Shop.objects.get(user=request.user)
        print(shop.location)
        
        product_form=ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            
            profile=product_form.save(commit=False)
            profile.shop=shop
            profile.location=shop.location
            profile.save()
            messages.success(request,'Product added successfully')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        product_form=ProductForm()
    return render(request,'product/create_product.html',{'product_form':product_form})

def product_list1(request):
    list=Product.objects.all().order_by('-created')
    return render(request,'product/product_list.html',{'list':list})


def update_product(request,id):
    Update = Product.objects.get(id=id)
    print(Update)
    form= ProductForm(instance=Update)
    if request.method=='POST':
        form= ProductForm(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('view_my_products')
    return render(request,'product/product_edit.html',{'form':form,'product':Update})

def delete_product(request,id):
    deleteemp = Product.objects.get(id=id)
    deleteemp.delete()
    messages.success(request,'Record deleted succefully')
    return redirect('view_my_products')

#product deatils

def product(request,category_slug=None):
    category = None
    
    products = Product.objects.filter(is_available=True)
    
    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(1)
    is_authenticated = request.user.is_authenticated
    print(is_authenticated)
    if is_authenticated:
        # wishlist = Wishlist.objects.filter(user=request.user)

        return render(
            request,
            'product/product.html',
            {
                'category': category,
                
                'products': products,
                # 'wishlist': wishlist
            }
        )

    else:
        return render(
            request,
            'product/product.html',
            {
                'category': category,
                
                'products': products,
            }
        )





def product_search(request):
    results = None
    try:
        query = request.POST['query']
        results = Product.objects.filter(name__icontains=query) |\
            Product.objects.filter(description__icontains=query)
        page = request.GET.get('page')
        paginator = Paginator(results, 6)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(1)
        return render(
            request,
            'product/product.html',
            {'products': results}
        )
    except KeyError:
        wishlist = None
        "KeyError"
        return render(
            request,
            'product/product.html',
            {'products': results}
        )

def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id,
        is_available=True
    )

    return render(
        request,
        'product/detail.html',
        {'product': product}
    )




def view_my_products(request):
    my_products=Product.objects.filter(shop=request.user.shop)
    print(my_products)
    return render(request,'product/view_products.html',{'my_products':my_products})


def view_all_products(request):
    shop=Shop.objects.filter(location=request.user.customer.location)
    product_category=ShopCategory.objects.all()
    print(shop)
    if request.method=="GET":
        shop=Shop.objects.filter(location=request.user.customer.location)
        product_category=ShopCategory.objects.all()
        location=request.GET.get('location')
        category=request.GET.get('category')
        try:
            product=Product.objects.filter(location__icontains=location) and Product.objects.filter(category=category)
            print(product)
            return render(request,'product/view_products.html',{'products':product,'category':category})
        except:
            pass


    return render(request,'product/view_products.html',{'category':product_category})