from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib import auth
# Create your views here.


def showMessage(string):
    print("\n=========================================")
    print(string)
    print("=========================================\n")


def home(request):

    # is_authenticated
    if request.user.is_authenticated:
        # ModalName.objects.all()
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'index.html', context)
    else:
        return redirect('login')


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

        return redirect('home')


def edit_book(request, book_id):

    if request.method == 'GET':
        book = Book.objects.get(id=book_id)
        return render(request, 'editBook.html', {'book': book})

    if request.method == 'POST':
        book = Book.objects.get(id=book_id)

        book.title = request.POST['book-title']
        book.author = request.POST['book-author']
        book.pages = request.POST['book-pages']
        book.price = request.POST['book-price']

        book.save()
        return redirect("home")


def delete_book(request, book_id):

    if request.method == "GET":
        showMessage("Deleting book with id: " + str(book_id))
        book = Book.objects.get(id=book_id)
        book.delete()
    return redirect('home')


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('home')

        return HttpResponse("<h1>Username or Password is wrong...</h1>")


def logout(request):
    auth.logout(request)
    return redirect('login')
