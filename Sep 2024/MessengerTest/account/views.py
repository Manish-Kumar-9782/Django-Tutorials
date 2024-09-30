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
        username = request.POST.get("username")
        password = request.POST.get("password")

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
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        c_password = request.POST.get("c_password")

        if password != c_password:
            return render(request, "registration.html", {'error': 'Passwords do not match'})

        # testing that a user already exist or not with incoming username

        # if a username does not exist we will have another error if use .get method.
        # to solve this problem we will use filter method.
        # x_user = User.objects.get(username=username)

        x_user = User.objects.filter(username=username).first()

        if x_user:
            return render(request,  "registration.html", {'error': f'An account already exist with username: {username}'})

        # first create a user using User model by passing user information.
        user = User.objects.create_user(username, email, password)

        # after creating user we need to save it into database.
        user.save()

        return redirect("login")


def logout(request):
    auth.logout(request)
    return redirect("login")


def profile_view(request):

    if request.user.is_authenticated and request.method == "GET":
        return render(request, 'user-profile.html')


def updateProfile(request):

    if request.user.is_authenticated and request.method == "GET":
        return render(request,  'update-profile.html')

    if request.user.is_authenticated and request.method == "POST":

        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        print(request.POST)

        user = User.objects.get(id=request.user.id)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect("profile")
