from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from home.models import *


# Create your views here.
def test(request):
    return render(request,"home/base.html")

def loginpage(request):
    return render(request,"home/login.html")

def signuppage(request):
    if request.method == "POST":
        data = request.POST
        Name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(
            first_name=Name,
            username=username
            )
        user.set_password(password)
        user.save()

        return redirect('/login')
    return render(request,"home/signup.html")
