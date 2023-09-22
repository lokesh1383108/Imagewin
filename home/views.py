from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate, login
from home.models import *
from django.contrib import messages


# Create your views here.
def test(request):
    return render(request,"home/base.html")

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
             messages.error(request, "User  does not exist")
            
        user = authenticate(username = username, password= password)

        if user is None:
             messages.error(request, "Invalid credential")
             return redirect('/login')
        else:
            login(request,user)
            return redirect('/home')

        
             
    return render(request,"home/login.html")

def signuppage(request):
    if request.method == "POST":
        data = request.POST
        Name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username is already exists")
            return redirect('/signup')

        user = User.objects.create(
            first_name=Name,
            username=username
            )
        user.set_password(password)
        user.save()

        return redirect('/login')
    return render(request,"home/signup.html")

def homepage(request):
    return render(request,'home/home.html')

def upload_image(request):
    return render(request,'home/upload.html')
