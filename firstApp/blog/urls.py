from django.urls import path
from . import views
urlpatterns = [

    path("", view=views.home, name="home"),
    path("welcome/", view=views.welcome, name="welcome"),
    path("addEntry/", view=views.addEntry, name="addEntry"),
    path("login/", view=views.login, name="login"),
    path("registration/", view=views.register_account, name="register"),
    path("logout/", views.logout, name="logout"),

]
