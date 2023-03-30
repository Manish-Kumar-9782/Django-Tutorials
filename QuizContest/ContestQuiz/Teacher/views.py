from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from Student.models import Student
# Create your views here.

# ManishKumar@DateMonthFullYear


def createStudent(request):

    if request.method == "GET":
        form = StudentRegistrationForm()

        return render(request, "Teacher/createStudent.html", {"form": form})

    if request.method == "POST":

        if request.user.is_authenticated:
            if request.user.has_perm("Student.add_student"):
                # Student.add_Student
                print("user does have permission to add student")
            else:
                print("user does not have permission to add student")

        return redirect("home")
