from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse, name='browse'), #Browse all products
    path('<int:pid>/', views.product, name='product'), #View a specific product
    path('search/', views.search, name='search'), #Search for products
]