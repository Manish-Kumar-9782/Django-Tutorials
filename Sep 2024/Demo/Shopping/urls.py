from django.urls import path
from django.http import HttpResponse


def shopping_home(request):
    return HttpResponse("<h1>Welcome to the shopping home page</h1>")


urlpatterns = [
    path('', view=shopping_home, name='index'),
]
