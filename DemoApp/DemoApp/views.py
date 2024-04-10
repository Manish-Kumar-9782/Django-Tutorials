from django.http.response import HttpResponse
from django.shortcuts import render

# a python function is view if it takes a request object.
# and returns a Response object


def home(request):
    return render(request, "index.html")
