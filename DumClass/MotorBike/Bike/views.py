from django.shortcuts import render, redirect

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        return render(request, 'bike/home.html')

    return redirect('login')
