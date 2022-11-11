"""stuc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('allcourse/',views.allcourse,name='allcourse'),
    path('createcourse/',views.CreateCourse,name='createcourse'),
    path('updatecourse/<pk>/',views.U_Course,name='updatecourse'),
    path('coursedetail/<id>/',views.Coursedetail,name='coursedetail'),
    path('coursedelete/<id>/',views.Coursedelete,name='coursedelete'),

    path('c_coursevisitor/',views.c_Coursevisitor.as_view(),name='c_coursevisitor'),

    path('allcoursecareer/',views.allcoursecareer,name='allcoursecareer'),
    path('createcoursecareer/',views.CreateCoursecareer,name='createcoursecareer'),
    path('updatecoursecareer/<pk>/',views.U_Coursecareer,name='updatecoursecareer'),
    path('coursedetailcareer/<id>/',views.Coursecareerdetail,name='coursecareerdetail'),
    path('coursecareerdelete/<id>/',views.Coursecareerdelete,name='coursecareerdelete'),
    path('counselling/',views.counselling_view,name='counselling'),







]
