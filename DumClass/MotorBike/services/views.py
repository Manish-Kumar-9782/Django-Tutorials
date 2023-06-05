from django.shortcuts import render, redirect
from .models import Service, Parts
# Create your views here.


def add_service(request):

    if request.method == 'GET':
        return render(request,  'service_templates/addService.html')

    if request.method == 'POST':
        service = Service()

        print("User: ", request.user)

        service.insertDetails(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            lastUpdatedBy=request.user,
            registeredBy=request.user
        )

        return redirect('bike')


def add_parts(request):

    if request.method == 'GET':
        return render(request, 'service_templates/addParts.html')

    if request.method == 'POST':
        # name, price, company
        name = request.POST.get("name")
        price = request.POST.get("price")
        company = request.POST.get("company")
        image = request.FILES.get("image")

        part = Parts()

        part.insertDetails(name, price, company, image, request.user, True)
        return redirect('bike')
