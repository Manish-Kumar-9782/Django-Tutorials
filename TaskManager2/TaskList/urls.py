from django.urls import path

from .views import task_list, add_taskList, add_task, delete_task, delete_tasklist

urlpatterns = [
    path("", view=task_list, name="show_task_lists"),
    path("add", view=add_taskList, name="add_task_list"),
    path("add_task", view=add_task, name="add_task"),
    path("delete_task/<int:taskId>", view=delete_task, name="delete_task"),
    path("delete_tasklist/<int:taskListId>",
         view=delete_tasklist, name="delete_tasklist"),
]
