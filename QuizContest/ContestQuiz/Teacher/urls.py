from django.urls import path
from . import views
urlpatterns = [
    path("createStudent/", views.createStudent, name="createStudent")
]
