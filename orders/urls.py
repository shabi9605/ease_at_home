
from django.urls import path
from . import views
app_name='orders'

urlpatterns = [
   
    path('create/',views.order_create,name="order_create"),
    path('process/',views.order_save,name="order_save"),
    path('orderview/',views.orderview,name='orderview'),
    path('orderitemview/',views.orderitemview,name='orderitemview'),
    path('neworder/',views.neworder,name="neworder"),
    path('update_order/<int:id>/',views.update_order,name="update_order"),
    path('delete_order/<int:id>/',views.delete_order,name="delete_order"),
    path('view_orders',views.view_orders,name='view_orders'),


    
]
