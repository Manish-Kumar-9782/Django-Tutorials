from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from .forms import StudentForm
from .models import Student
# Create your views here.


def home(request):
    # to get data from database use Student.objects.all();

    if request.user.is_authenticated:
        students = Student.objects.all()
        return render(request, "home.html", {"Students": students})

    return HttpResponse("<h1> login Required</h1>")


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
                return HttpResponse("<h1>User is not authenticated</h1>")

    return redirect("home")
