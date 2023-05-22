from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("addBook", views.add_book, name='add_book'),
    path("editBook/<int:book_id>", views.edit_book, name='edit_book'),
]
