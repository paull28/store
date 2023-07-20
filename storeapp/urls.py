from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.browse, name='browse'), #Browse all products
    path('<int:pid>/', views.product, name='product'), #View a specific product
    path('search/', views.search, name='search'), #Search for products
    path('basket/', views.basket, name="basket"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout/order/', views.order_confirmation, name='order'),

    path('add/<int:pid>', views.add_to_basket, name='add'),
    path('del/<int:cid>', views.remove_from_basket, name='del'),
    path('clear/', views.clear_basket, name='clear'),

]