from django.urls import path
from .views import blog_form

urlpatterns = [
    path("blog_form/", view=blog_form, name="blog_form")
]
