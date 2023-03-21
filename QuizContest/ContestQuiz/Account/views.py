from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import auth
from Teacher.models import Teacher
from Student.models import Student

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        UserRelatedModel = None
        if request.session.get("user-type"):
            if request.session['user-type'] == 'teacher':

                try:
                    UserRelatedModel = Teacher.objects.get(
                        UserAccount_id=request.user.id)
                except Teacher.DoesNotExist:
                    return HttpResponse(f"<h1>{request.user.username} is not teacher.</h1>")

            elif request.session['user-type'] == 'student':
                try:
                    UserRelatedModel = Student.objects.get(
                        UserAccount_id=request.user.id)
                except Student.DoesNotExist:
                    return HttpResponse(f"<h1>{request.user.username} is not student.</h1>")

        return render(request, "Account/home.html", {"User": UserRelatedModel})

    return redirect("login")


def login(request):

    if request.method == "GET":
        # go to the login page
        return render(request, "Account/login.html")

    if request.method == "POST":
        # getting user information from login page.
        user = None
        request.session['user-type'] = None
        if request.POST.get("login-type") == "teacher":

            user = authenticate(request,
                                username=request.POST.get('user_name'),
                                password=request.POST.get("user_password")
                                )

            request.session["user-type"] = 'teacher'

        elif request.POST.get("login-type") == "student":

            user = authenticate(request,
                                username=request.POST.get('user_name'),
                                password=request.POST.get("user_password")
                                )

            request.session["user-type"] = 'student'

        else:
            user = authenticate(request,
                                username=request.POST.get('user_name'),
                                password=request.POST.get("user_password")
                                )

        if user:
            # process the login
            auth.login(request, user)
            return redirect("home")
        else:
            return HttpResponse("<h1>User Name or Password is wrong.</h1>")
