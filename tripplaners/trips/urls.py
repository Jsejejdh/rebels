from django.contrib import admin
from django.urls import path,include
from trips import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register,name="register"),
]