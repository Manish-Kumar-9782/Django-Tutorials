from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher

# Create your views here.


def viewTeachers(request):

    # to retrieve the data from model
    # objects all(), filter(), get(), exclude().

    Teachers = Teacher.objects.all()

    return render(request, "view-teachers.html", {"Teachers": Teachers})


def register(request):

    if request.method == "POST":

        # print("Current User: ", request.user)

        print("\n------------------------------\n")
        print("Teacher Name: ", request.POST['name'])
        print("Teacher Subject: ", request.POST['subject'])
        print("Teacher DOB: ", request.POST['dob'])
        print("Teacher Address: ", request.POST['address'])
        print("Teacher mobileNo: ", request.POST['mobileNo'])
        print("\n------------------------------\n")

        teacher = Teacher()

        teacher.Name = request.POST['name']
        teacher.Subject = request.POST['subject']
        teacher.Dob = request.POST['dob']
        teacher.Address = request.POST['address']
        teacher.MobileNo = request.POST['mobileNo']

        teacher.save()

    if request.method == "GET":

        print("request name: ", request.GET.get('name'))

    return render(request, "register-teacher.html")


def login(request):
    return HttpResponse("<h1>This is login Page</h1>")
