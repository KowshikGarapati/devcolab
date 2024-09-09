from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from .models import User


# Create your views here.
def hello(request):
    return HttpResponse(b'hello world!')

def verify(request):
    Username = request.POST.get("username")
    Password = request.POST.get("password")
    user = User.objects.get(username=Username)
    username = user.username
    pwd = user.password
    if Username == username and Password == pwd:
        return HttpResponse(b' login True')
    else:
        return HttpResponse(b'login False')
        
#@csrf_protect
def login(request):
    return render(request, 'login.html')

def profile(request, username):
    return render(request, "profile.html", {"username": username})

def home(request):
    return render(request, "home.html")

def register(request):
    newusername = request.GET.get("username")
    newpassword = request.GET.get("password")
    newconfirmpwd = request.GET.get("confirm password")
    if newpassword == newconfirmpwd:
        newuser = User(username=newusername, password=newpassword)
        #newuser.full_clean()
        newuser.save()
        global USER
        USER = newuser
        print(newusername  ,newpassword)
        """return redirect(home, {"user":newuser})"""
        #return render(request, 'home.html')
        return redirect(newuser.username)
    signup_url = reverse('signup')
    return redirect(signup_url)  
    

def signup(request):
    return render(request, "signup.html")
    
    