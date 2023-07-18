"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from storeapp import views

urlpatterns = [
    path('', lambda reuqest: redirect('store/', permanent=False)),
    path('store/', include('storeapp.urls')),
    path('admin/', admin.site.urls),
    #Account related URLs:
    path('accounts/', include('django.contrib.auth.urls')), #Accounts, used to login (accounts/login)
    path('accounts/', views.account, name='account'),
    path('accounts/signup/', views.RegisterUser.as_view(), name='signup_user'), #Signup page
    path('accounts/edit/', views.update_user, name="update_user"),
    path('accounts/delete/', views.delete_user, name="delete_user"),

    path('accounts/orders', views.orders, name='orders'),
]
