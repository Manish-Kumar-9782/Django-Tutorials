from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# a view inside Teacher section return a HttpResponse.
def home(request):
    return HttpResponse("<h1>This is home Page<h1>")


def login(request):
    return HttpResponse("<h1>This is login Page</h1>")
