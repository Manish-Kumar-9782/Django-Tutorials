
from django.urls import path
from .views import emp_view, add_employee, emp_update

urlpatterns = [
    path("", view=emp_view, name="emp_view"),
    path("add/", view=add_employee, name="add_emp"),
    path("modify/<int:emp_id>", view=emp_update, name="modify_emp"),

]
