from django.shortcuts import render, redirect
from .models import TaskList, Task

# Create your views here.


def task_list(request):
    taskLists = TaskList.objects.all()  # get all taskLists from database
    return render(request, "home.html", {"taskLists": taskLists})


def add_taskList(request):

    if request.method == "GET":
        return render(request, "add_taskList.html")

    if request.method == "POST":
        # here we will process form data.
        title = request.POST.get("title")
        category = request.POST.get("category")

        task_list = TaskList(title=title, category=category)
        task_list.save()
        return redirect("show_task_lists")


# another function to  add a task.
def add_task(request):

    if request.method == "POST":
        text = request.POST.get("text")
        taskListId = request.POST.get("taskListId")

        # retrieve TaskList using taskListId.
        taskList = TaskList.objects.get(id=taskListId)

        # creating a new task.
        task = Task(text=text, task_list=taskList)
        task.save()

        return redirect("show_task_lists")
