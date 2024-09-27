from django.urls import path
from .views import login, register, logout, profile_view

urlpatterns = [
    path("login", view=login, name="login"),
    path("register", view=register, name="register"),
    path("logout", view=logout, name='logout'),
    path("profile", view=profile_view, name='profile'),

]
