from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('registeruser',views.registeruser,name='register'),
    path('login',views.loginuser, name='loginuser'),
    path('logout',views.logoutuser, name='logout')
]
