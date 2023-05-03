from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages
from .forms import StudentForm
from .models import Student
# Create your views here.


def home(request):
    # to get data from database use Student.objects.all();

    if request.user.is_authenticated:
        students = Student.objects.all()
        return render(request, "home.html", {"Students": students})

    return redirect("login")


def addStudent(request):

    if request.method == "GET":
        form = StudentForm()  # blank student form
        return render(request, "addStudent.html", {"form": form})

    if request.method == "POST":
        print(request.POST)  # filled student form with request.POST Data.
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("home")


def logout(request):
    print("logging out...")
    auth.logout(request)
    return redirect("home")


def removeStudent(request, pk):
    # pk primary key
    if request.method == "GET":
        print("button pressed: ", pk)
        st = Student.objects.get(pk=pk)
        st.delete()
        print("Student with id: ", pk, " Deleted")
    return redirect("home")


def updateStudent(request):
    return redirect("home")


def login(request):

    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = auth.authenticate(
                request, username=username, password=password)

            if user:
                auth.login(request, user)
            else:
                messages.error(request, "Username or password is incorrect")
                return redirect("login")

    return redirect("home")
