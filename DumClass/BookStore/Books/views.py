from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')


def add_book(request):
    
    if request.method == "GET":
        print("sending add book page to the client....")
        return render(request, 'addBook.html')
        
    if request.method == "POST":
        print("receiving add book request from the client....")
        
        print("Receiving Data: ", request.POST)
        return render(request, 'index.html')
    
