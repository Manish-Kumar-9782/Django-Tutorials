from django.shortcuts import render

# Create your views here.


def user_registration(request):

    print("request data: ", request.GET)

    username = request.GET["username"]
    phone_number = request.GET["phone_number"]
    email = request.GET["email"]
    password = request.GET["password"]
    c_password = request.GET["c_password"]

    print("Name : ", username)
    print("phone_number : ", phone_number)
    print("email : ", email)
    print("password : ", password)
    print("c_password : ", c_password)

    return render(request, "html_pages/userRegistration.html")


def table_extra(request):

    return render(request, "html_pages/table_extra.html")


def button_test(request):
    return render(request, "html_pages/button.html")


def position_property(request):
    return render(request, "html_pages/position.html")


def card_example_1(request):
    return render(request, "html_pages/card_example1.html")
