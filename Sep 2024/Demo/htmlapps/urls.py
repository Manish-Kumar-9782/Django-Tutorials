from django.urls import path
from .views import table_extra, button_test, position_property, card_example_1, user_registration, login, logout

urlpatterns = [
    path("table_extra", view=table_extra, name='table_extra'),
    path("button_test", view=button_test, name='button_test'),
    path("position_property", view=position_property, name='position_property'),
    path("card_example_1", view=card_example_1, name='card_example_1'),
    path("user_registration", view=user_registration, name='user_registration'),
    path("login", view=login, name='login'),
    path("logout", view=logout, name='logout'),
]
