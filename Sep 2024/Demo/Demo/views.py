from django.http import HttpResponse  # not in use
from django.shortcuts import render
from .data import myContent


def home_page(request):
    return render(request, "home_page.html")


def about_page(request):
    return render(request, "About.html")


def records_page(request):

    groups = {
        "20_to_30": 0,
        "30_to_40": 0,
        "40_plus": 0
    }


# create age groups
    for person in myContent:

        if person["age"] >= 20 and person["age"] < 30:
            groups["20_to_30"] += 1
        elif person["age"] >= 30 and person["age"] < 40:
            groups["30_to_40"] += 1
        elif person["age"] > 40:
            groups["40_plus"] += 1

    # now i don't want to use HttpResponse
    return render(request, "records.html", {"Persons": myContent, "ageGroups": groups})
