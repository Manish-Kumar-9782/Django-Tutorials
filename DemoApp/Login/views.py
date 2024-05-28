from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.


def login(request):

    print(dir(request.user))
    if request.method == 'GET':
        return render(request, "Login.html")

    if request.method == 'POST':
        # first get the data
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("User: %s" % user, " is Authenticated..")
            auth.login(request, user)
            return redirect("home")

        return HttpResponse("No Account found for username: " + username)


def logout(request):
    auth.logout(request)
    return redirect("home")


def register(request):

    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":

        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        c_password = request.POST.get("c_password")

        if password != c_password:
            return HttpResponse("Password does not match")

        user = User.objects.create_user(
            username, email, password,
            first_name=firstname, last_name=lastname)

        user.save()

        return redirect("login")
