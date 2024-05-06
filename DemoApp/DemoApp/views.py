from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import auth


# a python function is view if it takes a request object.
# and returns a Response object


def home(request):

    # first get the data from post

    return render(request, "index.html")
