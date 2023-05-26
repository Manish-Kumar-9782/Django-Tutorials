from django.shortcuts import render, redirect
from .models import Student_Information
# =============================================
from django.http import HttpResponse
# =============================================

# Create your views here.

# =============================================


def home(request):
    students = Student_Information.objects.all()
    print("All: ", students)
    context = {"students": students}
    return render(request, 'homepage.html', context)
# =============================================


def Student_Details(request):
    if request.method == "GET":
        return render(request, 'Student_Form.html')

    if request.method == "POST":
        student_name = request.POST["Student_name"]
        student_fatherName = request.POST["Student_fatherName"]
        student_city = request.POST["Student_city"]
        student_class = request.POST["Student_class"]
        student_mobileNumber = request.POST["Student_mobileNumber"]

        data = {
            'name': student_name, 'fatherName': student_fatherName,
            'city': student_city, 'cls': student_class,
            'mobileNumber': student_mobileNumber
        }

        print("Received Data: ", data)

        # student_Name
        # student_FatherName
        # student_City
        # student_Class
        # student_MobileNumber

        student = Student_Information()
        student.student_Name = student_name
        student.student_FatherName = student_fatherName
        student.student_City = student_city
        student.student_Class = student_class
        student.student_MobileNumber = student_mobileNumber
        student.save()

        return redirect('home')


def edit_Student(request, student_id):
    if request.method == "get":
        student = Student_Information.objects.get(id=student_id)
        return render(request, "editButton.html", {'student': student})

    if request.method == "POST":
        student = Student_Information.objects.get(id=student_id)

        student.name = request.POST["Student_name"]
        student.fatherName = request.POST["Student_fatherName"]
        student.city = request.POST["Student_city"]
        student.cls = request.POST["Student_class"]
        student.mobileNumber = request.POST["Student_mobileNumber"]

        student.save()
        return redirect("home")
