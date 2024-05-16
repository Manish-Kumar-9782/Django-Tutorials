from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def emp_view(request):

    employees = Employee.objects.all()

    return render(request, "view_employee.html", {"Employees": employees})


def add_employee(request):

    if request.method == "GET":
        return render(request, "employee_form.html")

    if request.method == "POST":

        _first_name = request.POST["first_name"]
        _last_name = request.POST["last_name"]
        _phone_number = request.POST["phone_number"]
        _email = request.POST["email"]

        emp = Employee(first_name=_first_name, last_name=_last_name,
                       phone_number=_phone_number, email=_email)
        emp.save()

    return redirect("emp_view")


def emp_update(request, emp_id):

    if request.method == "GET":
        emp = Employee.objects.get(id=emp_id)
        return render(request, "employee_form.html", {"update": True, "Emp": emp})

    if request.method == "POST":
        _first_name = request.POST["first_name"]
        _last_name = request.POST["last_name"]
        _phone_number = request.POST["phone_number"]
        _email = request.POST["email"]

        # Now i need to access the employee with id.
        emp = Employee.objects.get(id=emp_id)

        emp.first_name = _first_name
        emp.last_name = _last_name
        emp.phone_number = _phone_number
        emp.email = _email

        emp.save()

        return redirect("emp_view")


def emp_remove(request, emp_id):

    if request.method == "GET":
        Employee.objects.get(id=emp_id).delete()

    return redirect("emp_view")
