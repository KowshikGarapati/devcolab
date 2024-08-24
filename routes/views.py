from django.shortcuts import render
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
    print(request.POST.get("username"))
    return HttpResponse(b'home page')
    
    