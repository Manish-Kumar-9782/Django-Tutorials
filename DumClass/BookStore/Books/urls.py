from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("addBook", views.add_book, name='add_book')
]
