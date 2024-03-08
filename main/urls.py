from django.urls import path, re_path
from . import views
app_name = 'main'
urlpatterns = [


    path('', views.main, name='main'),
    path('menu/', views.ProductAPIView.as_view(), name='menu'),
    path('menu/category/<str:slug>', views.ProductAPIView.as_view(), name='menu_cat'),
    path('menu/page/<int:page>/', views.ProductAPIView.as_view(),  name='paginator'),
    path('cool_baskets/add/<int:product_id>/', views.cool_basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', views.cool_basket_remove, name='basket_remove'),
    path('basket', views.cool_profile, name='basket')

]