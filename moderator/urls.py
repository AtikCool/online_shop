from django.urls import path

from . import views

app_name= 'moder'
urlpatterns=[
    path('product_add/', views.product_add, name='product_add'),
    path('product_list', views.admin_product_list, name='admin_product_list'),
    path('product_update/<str:product_id>', views.update_product, name='product_update')]