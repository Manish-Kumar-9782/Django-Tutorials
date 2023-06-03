from django.urls import path
from . import views
urlpatterns = [
    path('addService', views.add_service, name='add_service'),
    path('addParts', views.add_parts, name='add_parts')
]
