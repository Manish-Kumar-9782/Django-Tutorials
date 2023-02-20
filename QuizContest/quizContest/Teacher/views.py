from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    if request.method == "POST":

        print("Posted data: ", request.POST.get('name'))

    if request.method == "GET":

        print("request name: ", request.GET.get('name'))

    return render(request, "index.html", {"name": "Manish Kumar"})


def login(request):
    return HttpResponse("<h1>This is login Page</h1>")
