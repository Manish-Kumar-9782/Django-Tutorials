from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

names = ["Kuldeep", "Karan", "Chandan", "Assis", "Asif"]

st = {
    "name": "Kuldeep",
    "age": 21,
    "height": 5.7
}


def home(request):
    return render(request, "home.html", {"name": "Manish", "Students": names, "age": 17, "student": st})
