from django.urls import path
from . import views
urlpatterns = [
    path('', views.login ),
    path('<str:username>/', views.profile, name='profile'),
    path('home/', views.home ),
    path('signup/', views.signup, name='signup'),
    path('signup/register/', views.register),
]
