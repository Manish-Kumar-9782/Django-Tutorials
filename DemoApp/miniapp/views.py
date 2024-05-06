from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


PersonList = [
    {
        "Name": "Manish Verma",
        "Age": 21,
        "Email": "manish00123@gmail.com",
        "Location": "Rajasthan",
        "Description": "Full Stack Web Developer",
        "Skills": ["C/C++", "Python", "Django", "Html", "CSS", "JavaScript", "React",]
    },
    {
        "Name": "Rahul Kumar",
        "Age": 21,
        "Email": "manish00123@gmail.com",
        "Location": "Rajasthan",
        "Description": "Full Stack Web Developer",
        "Skills": ["C/C++", "Python", "Django", "Html", "CSS", "JavaScript", "React",]
    },
    {
        "Name": "Aasish Pahatak",
        "Age": 21,
        "Email": "manish00123@gmail.com",
        "Location": "Rajasthan",
        "Description": "Full Stack Web Developer",
        "Skills": ["Python",  "Html", "CSS", "JavaScript"]
    }
]


def person_info(request):

    # handling for sending request
    # handling for sending post
    if request.method == "GET":
        return render(request, "person_form.html")

    if request.method == "POST":
        print("Request Data: ", request.POST)

        first_name = request.POST.get("first_name")
        second_name = request.POST.get("second_name")

        return HttpResponse(f"<h1>Full Name: {first_name + ' ' + second_name} </h1>")


def person_detail(request):

    if request.method == "GET":
        return render(request, "person_info.html", context={"Persons": PersonList})

    if request.method == "POST":
        pass


def person_detail(request):

    if request.method == "GET":
        return render(request, "person_card.html", context={"Persons": PersonList})

    if request.method == "POST":
        pass


def header(request):
    return render(request, "header.html")


def GotoLogin(request):
    return render(request, "GoTo_Login.html")


def login(request):
    return render(request, "Login.html")


def isPrime(request):
    n = int(request.GET.get("number", 0))
    # if number key is not found in the incoming request from
    # form then it will return 0.

    contextDict = {"isPrime": False, "number": n}
    print("number: ", n, type(n))
    if n < 2:
        contextDict.update({"isPrime": False})
        return render(request, "test2.html", contextDict)

    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                contextDict.update({"isPrime": False})
                return render(request, "test2.html", contextDict)

    contextDict.update({"isPrime": True})
    return render(request, "test2.html", contextDict)
