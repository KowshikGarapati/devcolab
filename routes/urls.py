from django.urls import path
from . import views
urlpatterns = [
    path('', views.login ),
    path('home/', views.home ),
    path('signup/', views.signup),
    path('signup/register/', views.register),
]
