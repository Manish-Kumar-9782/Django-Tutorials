from django.shortcuts import render, redirect, HttpResponse
from .models import TaskList, Task
# Create your views here.


def task_list(request):

    if request.method == "GET":
        taskLists = TaskList.objects.all()

        for task_list in taskLists:
            print(task_list.tasks.all())

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


def update_taskList_tasks(request):

    if request.method == "POST":
        taskListId = request.POST.get("taskListId")
        taskList = TaskList.objects.get(id=taskListId)

        for task in taskList.tasks.all():
            # assert isinstance(task, Task)

            task_isCompleted = bool(request.POST.get(f"task-{task.id}", False))

            # considering that not using javascript and only get values when checkbox
            # is checked.
            task.isCompleted = task_isCompleted  # updating task isCompleted status
            task.save()

        return redirect("view_tasks")


def delete_taskList(request, taskListId):

    if request.method == "POST":
        task = TaskList.objects.get(id=taskListId)
        task.delete()

        return redirect("view_tasks")

# =====================================================================#


def add_task(request, taskListId):
    # here weill save task_list's task in Task model
    # using TaskList object.
    if request.method == "POST":
        text = request.POST.get("text")
        # first retrieve the TaskList
        taskList = TaskList.objects.get(id=taskListId)
        task = Task(text=text, task_list=taskList)
        task.save()
        return redirect("view_tasks")

    return HttpResponse("<h1>Delete request only supports POST request</h1>")


def delete_task(request, taskId):

    if request.method == "GET":
        task = Task.objects.get(id=taskId)
        task.delete()
        return redirect("view_tasks")


def update_task(request, taskId):

    if request.method == "GET":
        task = Task.objects.get(id=taskId)
        # taskListId = task.task_list_id
        taskLists = TaskList.objects.all()

        return render(request, 'home.html',
                      {"taskLists": taskLists, "update": {
                          "task": task, "taskListId": task.task_list.id}},
                      )

    if request.method == "POST":
        text = request.POST.get("text")
        task = Task.objects.get(id=taskId)
        task.text = text
        task.save()
        return redirect("view_tasks")
