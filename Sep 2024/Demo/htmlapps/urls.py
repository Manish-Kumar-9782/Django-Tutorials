from django.urls import path
from .views import table_extra, button_test

urlpatterns = [
    path("table_extra", view=table_extra, name='table_extra'),
    path("button_test", view=button_test, name='button_test'),
]
