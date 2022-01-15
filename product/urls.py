from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('product_create',views.product_create,name='product_create'),
    path('product_list1',views.product_list1,name='product_list1'),
    path('delete_product/<int:id>',views.delete_product,name ='delete_product'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('product',views.product,name='product'),
    
    path('product_search', views.product_search, name='product_search'),
    path('product_detail<int:id>',views.product_detail, name='product_detail'),
    path('view_my_products',views.view_my_products,name='view_my_products'),
    path('view_all_products',views.view_all_products,name='view_all_products'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)