from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def login(request):

    # test that user is already logged in.
    if request.user.is_authenticated:
        return redirect('home')

    # if user not logged in
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":

        # print(request.POST)

        username = request.POST["username"]
        password = request.POST["password"]

        # print("username: ", username)
        # print("password: ", password)

        # testing that user information is correct and a genuine user exist.
        user = authenticate(request,  username=username, password=password)

        # if user information doest not match return to login with error message.
        if not user:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

        # if we have  a user, log them in and redirect to home page.
        # using auth.login function.
        auth.login(request, user)

        return redirect('home')


def register(request):

    if request.method == "GET":
        return render(request, "registration.html")

    if request.method == "POST":

        # retrieve data from POST  request.
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]

        if password != c_password:
            return render(request, "registration.html", {'error': 'Passwords do not match'})

        # first create a user using User model by passing user information.
        user = User.objects.create_user(username, email, password)

        # after creating user we need to save it into database.
        user.save()

        return redirect("login")
