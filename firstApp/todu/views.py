from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def jsBool(str):
    if str == 'true':
        return True
    elif str == 'false':
        return False
    return True


def home(request):

    if request.user.is_authenticated:
        # accessing only those todo items whose are belongs to the current user.
        todos = Todo.objects.filter(user_id=request.user.id)
        return render(request, "todo_home.html", {"todo_items": todos})
    else:
        return redirect("login")


def add_todo(request):

    if request.method == "POST":

        content = request.POST.get("content")
        todo = Todo()
        todo.content = content

        todo.user = request.user
        todo.save()

    return redirect('todu_home')


def update_todo(request, id):

    if request.method == "GET":

        item = Todo.objects.get(pk=id)
        return render(request, "update_todo.html", {"item": item})

    if request.method == "POST":
        content = request.POST.get("content")
        isCompleted = request.POST.get("isCompleted")

        item = Todo.objects.get(pk=id)

        if content:
            item.content = content

        # updating the completing status if only we have isCompleted value.
        if isCompleted:
            item.isCompleted = jsBool(isCompleted)

        item.save()

    return redirect("todu_home")


def delete_todo(request, id):

    if request.method == "GET":
        todo = Todo.objects.get(pk=id)
        todo.delete()

    return redirect("todu_home")
