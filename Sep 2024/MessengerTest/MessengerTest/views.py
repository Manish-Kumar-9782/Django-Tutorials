from django.shortcuts import render, redirect


def home(request):

    # first test that user is logged in .
    if request.user.is_authenticated:
        return render(request, 'home.html')

    return redirect("login")
