from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getHome, name='home'),
    path('', views.getLogin, name='login'),
]