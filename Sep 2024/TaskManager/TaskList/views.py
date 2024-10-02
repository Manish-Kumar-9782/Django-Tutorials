from django.shortcuts import render, redirect
from .models import TaskList
# Create your views here.


def task_list(request):

    if request.method == "GET":
        taskLists = TaskList.objects.all()
        return render(request, 'home.html', {"taskLists": taskLists})


def add_taskList(request):

    if request.method == "GET":
        return render(request, "tasks/add_task.html")

    if request.method == "POST":

        title = request.POST.get("title")
        category = request.POST.get("category")

        # create a task
        task = TaskList(title=title, category=category)
        task.save()

        return redirect("view_tasks")


def add_task(request, taskListId):
    # here weill save task_list's task in Task model
    # using TaskList object.
    pass
