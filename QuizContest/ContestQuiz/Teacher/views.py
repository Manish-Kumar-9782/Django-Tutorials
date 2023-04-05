from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from Student.models import Student
from django.contrib.auth.models import User
# Create your views here.

# ManishKumar@DateMonthFullYear


def createStudent(request):

    if request.method == "GET":
        form = StudentRegistrationForm()

        return render(request, "Teacher/createStudent.html", {"form": form})

    if request.method == "POST":

        if request.user.is_authenticated:
            if request.user.has_perm("Student.add_student"):
                # if user has permission to add student,
                student = Student()  # in this instance we will store our data taking from request
                # by using the form.
                form = StudentRegistrationForm(request.POST, instance=student)
                if form.is_valid():

                    # now if form is valid then we need to create a user account.
                    userName = request.POST.get("Name")
                    password = userName+"@" + \
                        "".join(request.POST.get("Dob").split("-"))

                    user = User.objects.create_user(username=userName,
                                                    password=password, email=request.POST.get("Email"))

                    student.UserAccount = user

                    user.save()
                    form.save()
                    return redirect("home")
                else:
                    return render(request, "Teacher/createStudent.html", {"form": form})

            else:
                print("user does not have permission to add student")

        return redirect("home")
