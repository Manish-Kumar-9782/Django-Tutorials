from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages
from Teacher.models import Teacher
from Student.models import Student


# Create your views here.


def home(request):

    if request.user.is_authenticated:
        UserRelatedModel = None
        print("user-type: ",  request.session.get("user-type"))
        # if request.session.get("user-type"):
        #     if request.session['user-type'] == 'teacher':
        #         try:
        #             UserRelatedModel = Teacher.objects.get(
        #                 UserAccount_id=request.user.id)
        #         except Teacher.DoesNotExist:
        #             messages.error(
        #                 request, f"{request.user.username} is not a teacher")

        #             return render(request, "Account/login.html")

        #     elif request.session['user-type'] == 'student':
        #         try:
        #             UserRelatedModel = Student.objects.get(
        #                 UserAccount_id=request.user.id)
        #         except Student.DoesNotExist:
        #             messages.error(
        #                 request, f"{request.user.username} is not a student")

        #             return render(request, "Account/login.html")

        return render(request, "Account/home.html", {"User": UserRelatedModel})

    return redirect("login")


def login(request):

    print("logging in...")
    if request.method == "GET":
        # go to the login page
        resetUserType(request)
        return render(request, "Account/login.html")

    if request.method == "POST":
        # getting user information from login page.
        resetUserType(request)
        user = None
        print(request.POST)

        user = authenticate(request,
                            username=request.POST.get('user_name'),
                            password=request.POST.get("user_password")
                            )

        if user:
            # process the login
            request.session["user-type"] = request.POST.get('login-type')

            if request.session.get("user-type"):
                if request.session['user-type'] == 'teacher':
                    try:
                        UserRelatedModel = Teacher.objects.get(
                            UserAccount_id=user.id)
                    except Teacher.DoesNotExist:
                        messages.error(
                            request, f"{request.POST.get('user_name')} is not a teacher")

                        return render(request, "Account/login.html", )

                elif request.session['user-type'] == 'student':
                    try:
                        UserRelatedModel = Student.objects.get(
                            UserAccount_id=user.id)
                    except Student.DoesNotExist:
                        messages.error(
                            request, f"{request.POST.get('user_name')} is not a student")

                        return render(request, "Account/login.html")

            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "User name of password is wrong")
            return render(request, "Account/login.html")


def resetUserType(request):
    if request.session.get('user-type'):
        del request.session['user-type']


def logout(request):

    if request.user:
        auth.logout(request)

    return redirect("home")
