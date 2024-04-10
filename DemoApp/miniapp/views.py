from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def person_info(request):

    # handling for sending request
    # handling for sending post
    if request.method == "GET":
        return render(request, "person_form.html")

    if request.method == "POST":
        print("Request Data: ", request.POST)
        fullname = request.POST.get("first_name") + \
            " " + request.POST.get("second_name")

        return HttpResponse(f"<h1>Full Name: {fullname} </h1>")
