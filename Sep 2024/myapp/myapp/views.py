from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def news1(request):
    return render(request, 'news/news1.html')
