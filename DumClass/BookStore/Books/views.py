from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.


def home(request):
    return render(request, 'index.html')


def add_book(request):

    if request.method == "GET":
        print("sending add book page to the client....")
        return render(request, 'addBook.html')

    if request.method == "POST":
        print("receiving add book request from the client....")
        print("\n\n==============================================")
        # print("Receiving Data: ", request.POST)
        # book-title, book-author, book-price, book-pages
        bookTitle = request.POST['book-title']
        bookAuthor = request.POST['book-author']
        bookPages = request.POST['book-pages']
        bookPrice = request.POST['book-price']

        data = {'title': bookTitle, 'author': bookAuthor,
                'pages': bookPages, 'price': bookPrice}

        print("received book Data: ", data)

        book = Book()
        book.title = bookTitle
        book.author = bookAuthor
        book.pages = bookPages
        book.price = bookPrice
        book.save()

        print("==============================================\n\n")

        return render(request, 'index.html')
