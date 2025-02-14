from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login

from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

    return render(request, "register.html")

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')


    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return render(request,'login.html')
# Create your views here.


