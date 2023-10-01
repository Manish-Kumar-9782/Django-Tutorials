from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from .models import MyUsers


def home(request):

    if (request.user.is_authenticated):
        return render(request, "index.html")

    return redirect("login")


def welcome(request):

    web_details = {
        "name": "Facebook",
        "views": 340,
        "author": "bhanu"
    }

    return render(request, "login.html", {"data": web_details})


def addEntry(request):

    if request.method == "GET":
        print("sending add Entry template....")
        return render(request, "addEntry.html")

    if request.method == "POST":
        print("processing add Entry data...")
        user = MyUsers()

        user.firstName = request.POST.get("firstName")
        user.lastName = request.POST.get("lastName")
        user.email = request.POST.get("email")

        user.save()

        return HttpResponse("Request Submitted...")


def login(request):

    if request.method == "GET":

        if not request.user.is_authenticated:
            return render(request, "login.html")

        return redirect("home")

    if request.method == "POST":
        _username = request.POST.get("username")
        _password = request.POST.get("password")

        user = auth.authenticate(
            request, username=_username, password=_password)

        if user:
            auth.login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or password incorrect.")


def logout(request):

    if request.method == "GET":
        auth.logout(request)

    return redirect("login")


def register_account(request):

    if request.method == "GET":
        return render(request, "Registration.html")

    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        email = request.POST.get("email")
        confirm_password = request.POST.get("cpassword")

        if (password == confirm_password):
            user = User.objects.create_user(
                username, email, password,
                first_name=firstname, last_name=lastname)

            user.save()
            return HttpResponse("Registration successful..")

        return HttpResponse("Password mismatch")


def showUsers(users):
    print("{:20s}{:20s}{:20s}".format("Name", "Age", "height"))

    for user in users:
        print("{:20s}{:20s}{:20s}".format(
            user.firstName, user.lastName, user.email))
