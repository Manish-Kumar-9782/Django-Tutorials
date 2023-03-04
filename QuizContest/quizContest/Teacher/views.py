from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Teacher

# Create your views here.


def viewTeachers(request):

    # to retrieve the data from model
    # objects all(), filter(), get(), exclude().

    Teachers = Teacher.objects.all()

    return render(request, "view-teachers.html", {"Teachers": Teachers})


def editTeacher(request, pk):

    if request.method == 'GET':
        print("found get request for teacher: ", pk)

        # Now we need to fetch the data from data base.
        teacher = Teacher.objects.get(pk=pk)
        return render(request, "edit-teachers.html", {"Teacher": teacher})
        # here we must need to return the request

    elif request.method == 'POST':
        print("found a teacher Editing request with data", request.POST)
        teacher = Teacher.objects.get(pk=pk)

        teacher.Name = request.POST.get("name", "-")
        teacher.Dob = request.POST.get("dob", "-")
        teacher.Subject = request.POST.get("subject", "-")
        teacher.Address = request.POST.get("address", "-")
        teacher.MobileNo = request.POST.get("mobileNo", "-")
        teacher.save()
        return redirect("view-teachers")

    else:
        pass

    return redirect("view-teachers")


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
