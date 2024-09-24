from django.urls import path
from .views import add_post

urlpatterns = [
    path("add",  view=add_post, name="add_post"),
]
