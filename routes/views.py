from django.shortcuts import redirect, render
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

def home(request):
    return render(request, "profile.html", {"user":None})

def register(request):
    newusername = request.GET.get("username")
    newpassword = request.GET.get("password")
    newuser = User(username=newusername, password=newpassword)
    newuser.full_clean()
    newuser.save()
    print(newusername  ,newpassword)
    """return redirect(home, {"user":newuser})"""
    return HttpResponse(b'register')
    

def signup(request):
    return render(request, "signup.html")
    
    