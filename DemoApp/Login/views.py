from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
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
