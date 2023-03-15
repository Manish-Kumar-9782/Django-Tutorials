from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import auth

# Create your views here.


def home(request):

    if request.user.is_authenticated:

        return HttpResponse("home section")

    return redirect("login")


def login(request):

    if request.method == "GET":
        # go to the login page
        return render(request, "Account/login.html")

    if request.method == "POST":
        # getting user information from login page.
        user = authenticate(request,
                            username=request.POST.get('user_name'),
                            password=request.POST.get("user_password")
                            )

        if user:
            # process the login
            auth.login(request, user)
            return redirect("home")
