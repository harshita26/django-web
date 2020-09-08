from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
   if request.method=='POST':
      username=request.POST['user']
      password=request.POST['pass']

      user=auth.authenticate(username=username, password=password)
      if user is not None:
         auth.login(request, user)
         messages.info(request,'The user is login')
         print('login')
         return redirect('/')
      else:
         messages.info(request,'The username and password does not match')
         print('The username and password does not match')
         return redirect('login')
   else:
      return render(request,'login.html')


def register(request):
   if request.method=='POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      password1=request.POST['password1']
      if password==password1:
         if User.objects.filter(username=username).exists():
            messages.info(request,'This username already taken')
            print("This username already taken")
            # return redirect('register')
            return render(request,'register.html')

         elif User.objects.filter(email=email).exists():
            messages.info(request,'This email address already taken')
            print("This email address already taken")
            return render(request,'register.html')
            # return redirect('register')

         else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.info(request,'User Created')
            print("User created")
            return redirect("login") 
      else:
         messages.info(request,'password not matching..')    
         print('Password Not match')
         return render(request,'register.html')
         # return redirect('register')
   else:
      return render(request,'register.html')

def logout(request):
   auth.logout(request)
   print('user logout')
   return redirect('/')