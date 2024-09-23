from django.urls import path
from . import views
urlpatterns = [
    path('', views.account ),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/home/', views.home, name='home' ),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/signup/register/', views.register, name='register'),
]
