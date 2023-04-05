from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.


def home(request):
    # to get data from database use Student.objects.all();
    students = Student.objects.all()
    return render(request, "home.html", {"Students": students})


def addStudent(request):

    if request.method == "GET":
        form = StudentForm()
        return render(request, "addStudent.html", {"form": form})

    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("home")
