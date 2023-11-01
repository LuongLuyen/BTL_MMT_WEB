from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getHome, name='home'), # tạo đường dẫn home/ thì vào trang home
    path('', views.getLogin, name='login'), #tạo đường dẫn mặc định thì vào trang login
]