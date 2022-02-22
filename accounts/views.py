
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User ,auth
from django.contrib import messages
import store
from django.db import models
from store.models import Customer

# Create your views here.

def login(request):
    if request.method== 'POST':
         username=request.POST['username']
         password=request.POST['password']

         user= auth.authenticate(username=username,password=password)
         if user is not None:
             auth.login(request, user)
             if Customer.objects.filter(name=user.username).exists() :
                 user.save();
             else:
                 customer=Customer.objects.create(user=user,name=user.username,email=user.email)
                 user.save();
             return redirect('store')
         else:
             messages.info(request,'invalid credentials')   
             return redirect('login') 
        

    else:
          return render(request,'store/login.html')





def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email exists already")
                 return redirect('register')
            else:        
                 user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                 user.save();
                 print("user created")
        else:
            messages.info(request,"password not matching..")
            return redirect('register')
            
        return redirect('login')

        
        
    else:    
        return render(request,'store/register.html')
        