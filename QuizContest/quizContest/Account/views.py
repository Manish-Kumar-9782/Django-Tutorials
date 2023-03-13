from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.


def home(request):

    # if user is logged in then we will show a logged in message for now.
    print("inside the home page")
    if request.user.is_authenticated:
        print("You are logged in")
        return render(request, 'home.html', {"user": request.user})
    else:
        return redirect("login")


def login(request):

    if request.method == "POST":
        userName = request.POST.get("user_name")
        userPassword = request.POST.get("user_password")

        user = authenticate(request, username=userName, password=userPassword)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return HttpResponse("<h1>User Name or Password is wrong!</h1>")

    return render(request, 'Accounts/login.html')
