from django.shortcuts import render, redirect
from .models import TaskList

# Create your views here.


def task_list(request):

    return render(request, "index.html")


def add_task(request):

    if request.method == "GET":
        return render(request, "add_task.html")

    if request.method == "POST":
        # here we will process form data.
        title = request.POST.get("title")
        category = request.POST.get("category")

        task_list = TaskList(title=title, category=category)
        task_list.save()
        return redirect("show_task_lists")
