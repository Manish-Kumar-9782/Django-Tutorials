from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


# logout view

def logout(request):
    auth.logout(request)
    return redirect('home_page')


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if not user:
            return render(request, "login.html", {"error": "Invalid Username or Password..!"})

        # if user is valid
        auth.login(request, user)

        # sending user from login page to home page after completion of login process.
        return redirect("home_page")


def user_registration(request):

    if request.method == "GET":
        return render(request, "html_pages/userRegistration.html")

    if request.method == "POST":

        print("request data: ", request.POST)

        username = request.POST["username"]
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]

        # checking that password is matched
        if password != c_password:
            return render(request, "html_pages/userRegistration.html",  {"error": "Passwords do not match"})

        # creating a new user entry using User Model.
        user = User.objects.create_user(username, email, password)
        user.save()

        return HttpResponse("User created successfully")


def table_extra(request):

    return render(request, "html_pages/table_extra.html")


def button_test(request):
    return render(request, "html_pages/button.html")


def position_property(request):
    return render(request, "html_pages/position.html")


def card_example_1(request):
    return render(request, "html_pages/card_example1.html")
