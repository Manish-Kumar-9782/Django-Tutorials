from django.shortcuts import render

# Create your views here.


def add_service(request):

    if request.method == 'GET':
        return render(request,  'service_templates/addService.html')
