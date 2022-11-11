import imp
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .serializers import CoursevisitorSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
import requests
from django.db.models import Q

USER_PER_PAGE=8
# Create your views here.
def allcourse(request):
    context={}
    query=""
    if request.GET:

        query=request.GET.get('q','')
        context['query']=str(query)
        if query:
            usersdata=course.objects.filter(title__contains=query)
            context['usersdata']=usersdata
            return render(request,'course/allcourse.html',context)

    usersdata=course.objects.all()

    page=request.GET.get('page',1)
    users_paginator=Paginator(usersdata,USER_PER_PAGE)

    try:
        usersdata=users_paginator.page(page)
    except PageNotAnInteger:
         usersdata=users_paginator.page(USER_PER_PAGE)
    except EmptyPage:
        usersdata=users_paginator.page(users_paginator.numpages)

    context['usersdata']=usersdata
    return render(request,'course/allcourse.html',context)

def Coursedetail(request,id=None):
    context={}
    url = 'http://127.0.0.1:8000/course/c_coursevisitor/'
    myobj = {'course_name': id}

    x = requests.post(url, json = myobj)

    print(x.text)
    user=course.objects.filter(id=id).values().first()
    context['data']=user

    return render(request,'course/coursedetail.html',context)


def U_Course(request,pk): 
    context={}

    if request.method=="POST":
        pi=course.objects.get(pk=pk)
        form=CourseForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request,"Update successful")
            return redirect('allcourse')
      
    pi=course.objects.get(pk=pk)
    form=CourseForm(instance=pi)
    context['form']=form
    return render(request,'course/add.html',context)

def CreateCourse(request):
    context={}

    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Added !')
            return redirect('allcourse')

        else:
            context['form']=form
            messages.error(request, 'Course not added !')
    else:
        form=CourseForm()
        context['form']=form
    return render(request,'course/add.html',context)

def Coursedelete(request,id=None):
    u=course.objects.get(id=id)
    u.delete()
    context={}
    messages.success(request, 'Deleted !')

    return redirect('allcourse')

class c_Coursevisitor(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=coursevisitor.objects.all()
    serializer_class=CoursevisitorSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def  post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


def allcoursecareer(request):
    context={}
    query=""
    if request.GET:

        query=request.GET.get('q','')
        context['query']=str(query)
        if query:
            usersdata=coursecareer.objects.filter(title__contains=query)
            context['usersdata']=usersdata
            return render(request,'course/allcoursecareer.html',context)

    usersdata=coursecareer.objects.all()

    page=request.GET.get('page',1)
    users_paginator=Paginator(usersdata,USER_PER_PAGE)

    try:
        usersdata=users_paginator.page(page)
    except PageNotAnInteger:
         usersdata=users_paginator.page(USER_PER_PAGE)
    except EmptyPage:
        usersdata=users_paginator.page(users_paginator.numpages)

    context['usersdata']=usersdata
    return render(request,'course/allcoursecareer.html',context)

def Coursecareerdetail(request,id=None):
    context={}
    # url = 'http://127.0.0.1:8000/course/c_coursevisitor/'
    # myobj = {'course_name': id}

    # x = requests.post(url, json = myobj)

    # print(x.text)
    user=coursecareer.objects.filter(id=id).values().first()
    context['data']=user

    return render(request,'course/coursecareerdetail.html',context)


def U_Coursecareer(request,pk): 
    context={}

    if request.method=="POST":
        pi=coursecareer.objects.get(pk=pk)
        form=CoursecareerForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request,"Update successful")
            return redirect('allcourse')
      
    pi=coursecareer.objects.get(pk=pk)
    form=CoursecareerForm(instance=pi)
    context['form']=form
    return render(request,'course/add.html',context)

def CreateCoursecareer(request):
    context={}

    if request.method=="POST":
        form=CoursecareerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Added !')
            return redirect('allcourse')

        else:
            context['form']=form
            messages.error(request, 'Course not added !')
    else:
        form=CoursecareerForm()
        context['form']=form
    return render(request,'course/add.html',context)

def Coursecareerdelete(request,id=None):
    u=coursecareer.objects.get(id=id)
    u.delete()
    context={}
    messages.success(request, 'Deleted !')

    return redirect('allcourse')



def counselling_view(request):
    context={}

    if request.method=="POST":
        skill=request.POST.get('skill')
        interest=request.POST.get('interest')
        courses=course.objects.filter(Q(course_name__icontains=skill) | Q(course_name__icontains=interest) | Q(title__icontains=skill) | Q(title__icontains=interest) ).order_by('title')
        
        careers=coursecareer.objects.filter(Q(skill__icontains=skill) | Q(skill__icontains=interest) | Q(career_name__icontains=skill) |Q(career_name__icontains=interest) ).order_by('career_name')    

        context['courses']=courses
        context['careers']=careers

        return render(request,'course/counsellingresult.html',context)


        

    return render(request,'course/counselling.html',context)



