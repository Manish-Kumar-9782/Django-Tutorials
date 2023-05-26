from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("Student_Details",views.Student_Details,name="Student_Details"),
    path("editButton/<int:student_id",views.edit_Student,name="edit_Student"),
]