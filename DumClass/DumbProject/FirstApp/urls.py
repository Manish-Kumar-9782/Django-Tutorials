from django.contrib import admin
from django.urls import path , include     
from . import views
# this is a list
urlpatterns = [
  path("", views.rootPage, name="root")
]