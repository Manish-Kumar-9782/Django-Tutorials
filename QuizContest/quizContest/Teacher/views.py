from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    if request.method == "POST":

        # print("Current User: ", request.user)

        print("\n------------------------------\n")
        print("Student Name: ", request.POST['name'])
        print("Student class: ", request.POST['class'])
        print("Student Section: ", request.POST['section'])
        print("Student Address: ", request.POST['address'])
        print("Student mobileNo: ", request.POST['mobileNo'])
        print("\n------------------------------\n")

    if request.method == "GET":

        print("request name: ", request.GET.get('name'))

    return render(request, "index.html", {"name": "Manish Kumar"})


def login(request):
    return HttpResponse("<h1>This is login Page</h1>")
