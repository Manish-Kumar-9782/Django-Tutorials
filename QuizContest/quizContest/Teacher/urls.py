from django.urls import path
from . import views

urlpatterns = [
    path("", views.viewTeachers, name="view-teachers"),
    path("register", views.register, name="register-teacher")
]
