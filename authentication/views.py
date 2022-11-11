import imp
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib import messages

# Create your views here.
def registraition_view(request):
    context={}

    if request.method=="POST":
        form=RegistratinForm(request.POST)
        print('reg form',form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfull.')
            return redirect('userlogin')

        else:
            context['form']=form
            messages.error(request, 'Registration Unsuccessfull')
    else:
        form=RegistratinForm()
        context['form']=form
    return render(request,'authentication/registration.html',context)


def userLogin_view(request):
    context={}


    if request.method=='POST':
        form=UserLoginForm(request.POST)
        print('post',form)
        if form.is_valid():

            username=request.POST.get('username')
            print('usrname',username)
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            print('usr',user)
            if user:
                login(request,user)
                messages.success(request, 'Login successfull')
                return redirect('home')
        else:
            context['form']=UserLoginForm()
            messages.error(request, 'Login Unsuccessfull')
            redirect('userlogin')
    else:
        print('form')
        form=UserLoginForm()
    context['form']=form
    print('form',form)
    return render(request,'authentication/login.html',context)

def userLogout_view(request):
    logout(request)
    return redirect('/')

