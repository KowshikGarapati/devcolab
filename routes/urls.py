from django.urls import path
from . import views
urlpatterns = [
    path('', views.account ),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/home/', views.home, name='home' ),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/login/verify', views.verify, name='verify'),
    path('accounts/signup/register/', views.register, name='register'),
]
