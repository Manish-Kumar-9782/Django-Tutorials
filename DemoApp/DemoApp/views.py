from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth


# a python function is view if it takes a request object.
# and returns a Response object


def home(request):

    # first get the data from post
    if request.user.is_authenticated:
        return render(request, "index.html")

    return redirect("login")
