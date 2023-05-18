from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
import csv
import os
# Create your views here.

# a simple view for root page

# this is view function
def rootPage(request):
    students = Student.objects.all()
    return render(request, "index.html", {"items": students})
