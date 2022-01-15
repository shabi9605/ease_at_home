from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.index,name="index"),
    path('shop_register',views.shop_register,name="shop_register"),
    path('user_login',views.user_login,name='user_login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('home_servicer_register',views.home_servicer_register,name="home_servicer_register"),
    path('customer_register',views.customer_register,name="customer_register"),
    path('volunteer_register',views.volunteer_register,name='volunteer_register'),
    path('registrations',views.registrations,name='registrations'),
    path('volunteer',views.volunteer,name='volunteer'),
    path('update_volunteer/<int:volunteer_id>',views.update_volunteer,name='update_volunteer'),
    path('delete_volunteer/<int:id>',views.delete_volunteer,name='delete_volunteer'),
    path('home_servicers',views.home_servicers,name='home_servicers'),
    path('servicer_booking/<int:servicer_id>',views.servicer_booking,name='servicer_booking'),
    path('view_customer_bookings',views.view_customer_bookings,name='view_customer_bookings'),
    path('view_servicer_bookings',views.view_servicer_bookings,name='view_servicer_bookings'),
    path('delete_booking/<int:id>',views.delete_booking,name='delete_booking'),
    path('update_booking/<int:booking_id>',views.update_booking,name='update_booking'),
    path('volunteer_availability',views.update_availablity_volunteer,name='volunteer_availability'),
    path('servicer_availability',views.update_availablity_servicer,name='servicer_availability'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)