"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

# from .views import news_report_view

from django.conf.urls.static import static
from django.conf import settings
from .views import news_page, blog_form1


def home_view(request):
    return render(request, "index.html")


def house_view(request):
    return HttpResponse("<h1> hello world </h1>\
        <h2> hello guyzzz </h2>")


def bazar_view(request):
    return HttpResponse("<h1> aalu , bhindi , tamatar , palak </h1>")


def school_view(request):
    return HttpResponse("<h2> math , science , geo , history </h2>")


def homey_page(request):
    return render(request, "index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('house/', view=house_view, name='my home'),
    path('market/', view=bazar_view, name='our market'),
    path('school/', view=school_view, name='our school'),
    path('home/', view=home_view, name="ourhome"),
    path('homey/', view=homey_page),
    path('news/', view=news_page, name="news"),
    path('blog_form1/', view=blog_form1, name="blog_form1")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
