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
    if request.user.has_perm("services.add_parts"):
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
        return render(request, 'access_denied.html', {"perm": 'add'})


def edit_part(request, id):

    if request.user.has_perm("services.change_parts"):
        if request.method == "GET":
            # first get the part from database
            part = Parts.objects.get(id=id)
            return render(request, 'service_templates/editPart.html', {'part': part})

        if request.method == "POST":
            part = Parts.objects.get(id=id)
            name = request.POST.get("name")
            price = request.POST.get("price")
            company = request.POST.get("company")
            image = request.FILES.get("image")

            part.insertDetails(name, price, company,
                               image, request.user, False)
            return redirect('bike')
    return render(request, 'access_denied.html', {"perm": 'edit'})


def delete_part(request, id):
    if request.user.has_perm("services.delete_parts"):
        if request.user.is_authenticated:
            part = Parts.objects.get(id=id)
            part.delete()
            return redirect('bike')

    return render(request, 'access_denied.html', {"perm": 'delete'})


def permissions(user):

    print("add Permission: ", user.has_perm("services.add_parts"))
    print("change Permission: ", user.has_perm("services.change_parts"))
    print("delete Permission: ", user.has_perm("services.delete_parts"))
    print("view Permission: ", user.has_perm("services.view_parts"))
