from django.shortcuts import render

# Create your views here.


def table_extra(request):

    return render(request, "html_pages/table_extra.html")


def button_test(request):
    return render(request, "html_pages/button.html")
