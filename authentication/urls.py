from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.registraition_view,name='register'),
    path('login/',views.userLogin_view,name='userlogin'),
    path('logout/',views.userLogout_view,name='userlogout'),


]
