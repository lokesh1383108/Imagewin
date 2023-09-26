from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate, login, logout
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
            return redirect('/homePage')
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
    querySet = uploadimage.objects.all()
    context = {'image':querySet}
    guess_messages = {}
    if request.method == "POST":
        user_guess = request.POST.get('guess_location_name')
        # correct_location = request.session.get('correct_location')
        
        print("User Guess:", user_guess)
        for images in querySet:
            correct_location = images.location_name
            print("correct location: ", correct_location,"id->",images.id)
            guess_messages[images.id] = "Correct guess!" if user_guess == correct_location else "Wrong guess, try again."


        context['guess_messages'] = guess_messages
    
   
    return render(request,'home/homePage.html',context)
                                                                   
def upload_image(request):
    if request.method=="POST":
        data = request.POST
        location_name = request.POST.get('location_name')
        location_image = request.FILES.get('location_image')

        user= uploadimage.objects.create(
            location_name = location_name,
            location_image = location_image
        )
        request.session['correct_location'] = location_name
        # print("Correct location stored:", location_name)  #debug the

        return redirect('/homePage')
    
    return render(request,"home/upload.html")

def logout_page(request):
    logout(request)
    messages.success(request,"You are logged Out")
    return redirect('/login')

def user_update(request):
    queryset = User.objects.all()
    context = {'up':queryset}
    
    return render(request,"home/update.html",context)

