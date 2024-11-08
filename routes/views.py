from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from .models import User, UserProfile
import random, requests


# Create your views here.
def hello(request):
    return HttpResponse(b'hello world!')

def verify(request):
    Username = request.POST.get("username")
    Password = request.POST.get("password")
    user = User.objects.get(username=Username)
    #username = user.username
    #pwd = user.password
    if Username == user.username and Password == user.password:
        request.session["userprofile"] = UserProfile.objects.get(user=user)
        return redirect('/')
    else:
        return redirect('accounts/login/')
        
#@csrf_protect
def login(request):
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def account(request):
    userprofile = request.session.get('userprofile')
    if userprofile:
        return render(request, 'profile.html', {'userprofile': userprofile})
    else:
        return redirect(reverse('signup'))

def profile(request, username):

    try:
        UserProfile.objects.get(user=User.objects.get(username = username))
    except:
        return HttpResponse(b'no user named {username}')
    if username == request.session.get('userprofile').user.username :
        return redirect('/')
    return render(request, "profile2.html", {'userprofile': UserProfile.objects.get(user = User.objects.get(username=username))})

def home(request):
    return render(request, "home.html")

def register(request):
    global newusername, newpassword, newemail
    newusername = request.GET.get("username")
    newpassword = request.GET.get("password")
    newconfirmpwd = request.GET.get("confirm password")
    newemail = request.GET.get("mail")
    if newpassword == newconfirmpwd:
        if newemail in User.objects.values_list('email', flat=True):
            return HttpResponse(b'email already exists')
        else:
            return redirect('sendverificationemail', recipient=newemail)
        """newuser = User(username=newusername, password=newpassword, email=newemail)
        #newuser.full_clean()
        newuser.save()
        print(newusername  ,newpassword)
        request.session['userprofile'] = newuser"""
        """return redirect(home, {"user":newuser})"""
        #return render(request, 'home.html')
        return redirect('/emailverify')
    signup_url = reverse('signup')
    return redirect(signup_url)  


def send_verification_email(request):
    global otp
    otp = random.randint(10000, 99999)
    API_KEY = '5E75CD07C85BBFE9A85475B4EB1E46102E041EEC354083B208B11420D482F6FCA3CDB2B1DC2B060B99F8C2250B03A522'
    url = "https://api.elasticemail.com/v2/email/send"
    payload = {
            'apikey': API_KEY,
            'subject': 'verification code for your account registration',
            'from': 'kowshikgarapati@gmail.com',
            'to': request.GET.get('recipient'),
            'bodyHtml': f'<h1>{otp} is the OTP for your devcolab registration</h1>',
            'isTransactional': False
    }

        # Send a POST request to Elastic Email
    response = requests.post(url, data=payload)

        # Check response
    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print("Failed to send email:", response.json())
    return redirect('/verifyotp')


def verifyotp(request):
    return render(request, "otpverification.html")

def emailverify(request):
    entered_otp = request.GET.get("otp")
    if entered_otp == str(otp):
        user_created = User.objects.create(username=newusername, password=newpassword, email=newemail)
        request.session['id'] = user_created.id
        return redirect('account')
    else:
        return redirect('register')


def signup(request):
    return render(request, "signup.html")
    
    