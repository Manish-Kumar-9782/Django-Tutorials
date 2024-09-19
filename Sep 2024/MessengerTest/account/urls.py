from django.urls import path
from .views import login, register

urlpatterns = [
    path("login", view=login, name="login"),
    path("register", view=register, name="register"),
]
