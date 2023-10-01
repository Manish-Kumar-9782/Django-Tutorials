from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', view=views.home, name='todu_home'),
    path("add_todo", view=views.add_todo, name="add_todo"),
    path("update_todo/<int:id>", view=views.update_todo, name="update_todo"),
    path("delete_todo/<int:id>", view=views.delete_todo, name="delete_todo"),

]
