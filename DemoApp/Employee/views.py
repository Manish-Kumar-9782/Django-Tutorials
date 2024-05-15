from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def emp_view(request):

    employees = Employee.objects.all()

    return render(request, "view_employee.html", {"Employees": employees})


def add_employee(request):

    if request.method == "GET":
        return render(request, "add_employee.html")

    if request.method == "POST":

        _first_name = request.POST["first_name"]
        _last_name = request.POST["last_name"]
        _phone_number = request.POST["phone_number"]
        _email = request.POST["email"]

        emp = Employee(first_name=_first_name, last_name=_last_name,
                       phone_number=_phone_number, email=_email)
        emp.save()

    return HttpResponse("Hello, employee View")


def emp_update(request, emp_id):

    return HttpResponse(f"Modify employee by id: %s" % emp_id)
