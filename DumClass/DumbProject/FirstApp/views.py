from django.shortcuts import render
from django.http import HttpResponse
import csv
import os
# Create your views here.

# a simple view for root page


def rootPage(request):
    items = ["This is a very simple example", "our django is going very well",
             "this is good", "we have created the template", "connected the index html to the view"]
    # pass this list to render method as context
    # context is dict like object.
    context = {
        "items": items,
    }
    print("current root directory: ", os.getcwd())
    file = open("database.csv")

    header = file.readline().strip("\n")
    header = header.split(",")
    rows = []
    for i in range(30):
        row = file.readline().strip("\n")
        rows.append(row.split(","))

    context = {
        "header": header,
        "rows": rows,
        "items": items
    }
    return render(request, "index.html", context)
