
from django.urls import path, include
from .views import login, logout

urlpatterns = [
    path("", view=login, name="login"),
    path("logout/", view=logout, name="logout"),
]
