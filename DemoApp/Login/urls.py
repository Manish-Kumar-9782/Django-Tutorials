
from django.urls import path, include
from .views import login, logout, register

urlpatterns = [
    path("login/", view=login, name="login"),
    path("logout/", view=logout, name="logout"),
    path("register/", view=register, name="register")
]
