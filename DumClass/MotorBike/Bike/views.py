from django.shortcuts import render, redirect
from services.models import Service, Parts
# Create your views here.


def home(request):

    services = Service.objects.all()
    parts = Parts.objects.all()
    if request.user.is_authenticated:
        return render(request, 'bike/home.html',
                      {"services": services,
                       "parts": parts})

    return redirect('login')
