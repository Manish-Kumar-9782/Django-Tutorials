from django.shortcuts import render

from .models import Student

# Create your views here.


def register(request):

    if request.method == "POST":

        # print("Current User: ", request.user)

        print("\n------------------------------\n")
        print("Student Name: ", request.POST['name'])
        print("Student class: ", request.POST['class'])
        print("Student Section: ", request.POST['section'])
        print("Student Address: ", request.POST['address'])
        print("Student mobileNo: ", request.POST['mobileNo'])
        print("\n------------------------------\n")

        student = Student()

        student.Name = request.POST['name']
        student.Class = request.POST['class']
        student.Section = request.POST['section']
        student.Address = request.POST['address']
        student.MobileNo = request.POST['mobileNo']
        student.save()

    if request.method == "GET":

        print("request name: ", request.GET.get('name'))

    return render(request, "register-student.html")
