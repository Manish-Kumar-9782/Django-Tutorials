from django.shortcuts import render, redirect
from services.models import Service, Parts
# Create your views here.


def home(request):

    services = Service.objects.all()
    parts = Parts.objects.all()
    if request.user.is_authenticated:
        permissions = {
            'has_permission_add': request.user.has_perm("services.add_parts"),
            'has_permission_change': request.user.has_perm("services.change_parts"),
            'has_permission_delete': request.user.has_perm("services.delete_parts"),
            'has_permission_view': request.user.has_perm("services.view_parts"),
        }

        context = {"services": services,
                   "parts": parts}

        context.update(permissions)

        return render(request, 'bike/home.html', context)

    return redirect('login')
