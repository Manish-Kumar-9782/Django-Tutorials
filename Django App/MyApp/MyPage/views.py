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
        form = StudentForm()  # blank student form
        return render(request, "addStudent.html", {"form": form})

    if request.method == "POST":
        print(request.POST)  # filled student form with request.POST Data.
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("home")


def removeStudent(request, pk):

    if request.method == "GET":
        print("button pressed: ", pk)
        st = Student.objects.get(pk=pk)
        st.delete()
        print("Student with id: ", pk, " Deleted")
    return redirect("home")


def updateStudent(request):
    return redirect("home")
