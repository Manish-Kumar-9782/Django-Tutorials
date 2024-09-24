from django.urls import path
from .views import login, register, logout

urlpatterns = [
    path("login", view=login, name="login"),
    path("register", view=register, name="register"),
    path("logout", view=logout, name='logout')
]
