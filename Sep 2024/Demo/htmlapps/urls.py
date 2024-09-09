from django.urls import path
from .views import table_extra

urlpatterns = [
    path("table_extra", view=table_extra, name='table_extra')
]
