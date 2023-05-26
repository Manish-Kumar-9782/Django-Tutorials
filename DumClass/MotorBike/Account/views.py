from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.


def login(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('bike')
        return render(request, 'login.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        # if username and password are valid then only we will have a user object

        if user:
            auth.login(request, user)
            return redirect('bike')

    return HttpResponse("<h1> Bad Request </h1>")
