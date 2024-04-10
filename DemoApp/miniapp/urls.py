from django.urls import path
# path is used to create UrlResolver for urlsPatterns.
from .views import person_info

urlpatterns = [
    path("person_info/", view=person_info, name="person_info")
]
