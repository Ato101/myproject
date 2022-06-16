from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username).exist():
                messages.info(request,'user name already exist')
                return redirect('index')
            elif User.objects.filter(email).exist():
                messages.info(request,'email already exist')
                return redirect('index')
            else:
                user=User.objects.create_user(username=username,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password is the same')
    else:
        return render(request,'index.html')


def login(request):
     if request.method =='POST':
         username= request.POST['username']
         password= request.POST['password']
         user =auth.authenticate(username=username,password=password)

         if user is not None:
             auth.login(request,user)
             return redirect('/')
         else:
             messages.info(request,'invalid credentials')
             return redirect(request,'index' )

     else:
        return render(request,'login.html')


