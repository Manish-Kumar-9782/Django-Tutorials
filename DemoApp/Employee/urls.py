
from django.urls import path
from .views import emp_view, add_employee

urlpatterns = [
    path("", view=emp_view, name="emp_view"),
    path("add/", view=add_employee, name="add_emp"),

]
