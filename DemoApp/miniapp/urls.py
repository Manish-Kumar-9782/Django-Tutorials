from django.urls import path
# path is used to create UrlResolver for urlsPatterns.
from .views import person_info, person_detail, header, GotoLogin, login, isPrime

urlpatterns = [
    path("person_info/", view=person_info, name="person_info"),
    path("person_detail/", view=person_detail, name="person_detail"),
    path("person_cards/", view=person_detail, name="person_cards"),
    path("header/", view=header, name="header"),
    path("goto_login/", view=GotoLogin, name="goto_login"),
    path("login/", view=login, name="login"),
    path("isprime/", view=isPrime, name="isprime"),
]
