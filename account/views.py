from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')



def shop_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        shop_form=ShopRegisterForm(request.POST,request.FILES)
        if user_form.is_valid() and shop_form.is_valid():
            user=user_form.save()
            user.save()
            profile=shop_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         shop_form=ShopRegisterForm()
    return render(request,'shop_register.html',{'register':reg,'user_form':user_form,'shop_form':shop_form}) 




def home_servicer_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        homeservicer_form=HomeServicerRegisterForm(request.POST,request.FILES)
        if user_form.is_valid() and homeservicer_form.is_valid():
            user=user_form.save()
            user.save()
            profile=homeservicer_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         homeservicer_form=HomeServicerRegisterForm()
    return render(request,'homeservicer_register.html',{'register':reg,'user_form':user_form,'homeservicer_form':homeservicer_form}) 



def customer_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        customer_form=CustomerRegisterForm(request.POST,request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user=user_form.save()
            user.save()
            profile=customer_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         customer_form=CustomerRegisterForm()
    return render(request,'customer_register.html',{'register':reg,'user_form':user_form,'customer_form':customer_form}) 



def volunteer_register(request):
    reg=False
    if request.method=='POST':
        shop=Shop.objects.get(user=request.user)
        print(shop)
        user_form=UserForm(data=request.POST)
        volunteer_form=VolunteerRegisterForm(request.POST,request.FILES)
        if user_form.is_valid() and volunteer_form.is_valid():
            user=user_form.save()
            user.save()
            profile=volunteer_form.save(commit=False)

            profile.user=user
            profile.shop=shop
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         volunteer_form=VolunteerRegisterForm()
    return render(request,'volunteer_register.html',{'register':reg,'user_form':user_form,'volunteer_form':volunteer_form}) 



def registrations(request):
    return render(request,'registrations.html')




def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        
        return render(request,'login.html')


def dashboard(request):
    #list=Todo.objects.all()
    return render(request,'dashboard.html')



@login_required
def user_logout(request):
    logout(request)
    return redirect('index')



def volunteer(request):
    our_volunteer=Volunteer.objects.filter(shop=request.user.shop,availability_status='available')
    print(our_volunteer)
    return render(request,'our_volunteer.html',{'our_volunteer':our_volunteer})


def update_volunteer(request,volunteer_id):
    my_volunteer=Volunteer.objects.get(id=volunteer_id)
    if request.method=="POST":
        my_volunteer=Volunteer.objects.get(id=volunteer_id)
        update_form=UpdateForm(request.POST,instance=my_volunteer.user)
        
        update_profile_form=UpdateProfileForm(request.POST,instance=my_volunteer)
        
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=my_volunteer.user)
        update_profile_form=UpdateProfileForm(instance=my_volunteer)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'update_volunteer.html',context)



def delete_volunteer(request,id):
    deleteemp = Volunteer.objects.get(id=id)
    deleteemp.delete()
    messages.success(request,'Record deleted succefully')
    return redirect('volunteer')



def home_servicers(request):
    category=HomeServicerCategory.objects.all()
    if request.method=="GET":
        category=HomeServicerCategory.objects.all()
        location=request.GET.get('location')
        category1=request.GET.get('category')
        try:
            servicer=HomeServicer.objects.filter(location__icontains=location) and HomeServicer.objects.filter(category=category1,availability_status='available')
            print(servicer)
            return render(request,'home_servicers.html',{'servicer':servicer,'category':category})
        except:
            pass
        
    return render(request,'home_servicers.html',{'category':category})



def servicer_booking(request,servicer_id):
    servicer=HomeServicer.objects.get(id=servicer_id)
    if request.method=="POST":
        servicer=HomeServicer.objects.get(id=servicer_id)
        booking_form=BookingForm(request.POST)
        if booking_form.is_valid():
            bookings=Booking(customer=request.user.customer,wanted_date=booking_form.cleaned_data['wanted_date'],place=booking_form.cleaned_data['place'])
            bookings.servicer=servicer
            bookings.save()
            return redirect('view_customer_bookings')
        else:
            return HttpResponse("Invalid Form")
    booking_form=BookingForm()
    return render(request,'booking_form.html',{'booking_form':booking_form})


def view_customer_bookings(request):
    customer_bookings=Booking.objects.filter(customer=request.user.customer)
    
    print(customer_bookings)
    return render(request,'view_bookings.html',{'customer_bookings':customer_bookings})


def view_servicer_bookings(request):
    servicer_bookings=Booking.objects.filter(servicer=request.user.homeservicer)
    print(servicer_bookings)
    return render(request,'view_bookings.html',{'servicer_bookings':servicer_bookings})


def delete_booking(request,id):
    delete_booking = Booking.objects.get(id=id)
    delete_booking.delete()
    messages.success(request,'Record deleted succefully')
    return redirect('view_customer_bookings')


def update_booking(request,booking_id):
    booking=Booking.objects.get(id=booking_id)
    print(booking)
    update_booking_form=UpdateBookingForm(instance=booking)
    if request.method=="POST":
        update_booking_form=UpdateBookingForm(request.POST,request.FILES,instance=booking)
        update_booking_form.save()
        return redirect('view_servicer_bookings')
    return render(request,'update_bookings.html',{'update_booking_form':update_booking_form})



def update_availablity_volunteer(request):
    my_volunteer=Volunteer.objects.get(user=request.user)
    print(my_volunteer.availability_status)
    if request.method=="POST":
        my_volunteer=Volunteer.objects.get(user=request.user)
        update_form=VolunteerAvailabilityForm(request.POST,instance=my_volunteer)
        print(my_volunteer.availability_status)
        if update_form.is_valid():
            update_form.save()
            
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=VolunteerAvailabilityForm(instance=my_volunteer.user)
        
    context={
        'update_form':update_form,
        
    }
    return render(request,'update_volunteer_availability.html',context)



def update_availablity_servicer(request):
    my_servicer=HomeServicer.objects.get(user=request.user)
    print(my_servicer.availability_status)
    if request.method=="POST":
        my_servicer=HomeServicer.objects.get(user=request.user)
        update_form=ServicerAvailabilityForm(request.POST,instance=my_servicer)
        print(my_servicer.availability_status)
        if update_form.is_valid():
            update_form.save()
            
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=VolunteerAvailabilityForm(instance=my_servicer.user)
        
    context={
        'update_form':update_form,
        
    }
    return render(request,'update_servicer_availability.html',context)
