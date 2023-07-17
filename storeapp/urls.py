from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.browse, name='browse'), #Browse all products
    path('<int:pid>/', views.product, name='product'), #View a specific product
    path('search/', views.search, name='search'), #Search for products

    #Account related URLs:
    path('account/', include('django.contrib.auth.urls')), #Accounts, used to login (accounts/login)
    path('account/signup/', views.RegisterUser.as_view(), name='signup_user'), #Signup page
    path('account/edit/', views.updateUser, name="updateUser"),
    path('account/delete/', views.deleteUser, name="deleteUser"),

]