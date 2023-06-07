from django.urls import path
from . import views
urlpatterns = [
    path('addService', views.add_service, name='add_service'),
    path('addParts', views.add_parts, name='add_parts'),
    path('editPart/<int:id>', views.edit_part, name='edit_part'),
    path('deletePart/<int:id>', views.delete_part, name='delete_part'),
]
