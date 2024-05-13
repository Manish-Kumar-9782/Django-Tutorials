from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def emp_view(request):
    return HttpResponse("Hello, employee View")


def add_employee(request):

    if request.method == "GET":
        return render(request, "add_employee.html")

    if request.method == "POST":
        print(request.POST)

    return HttpResponse("Hello, employee View")
