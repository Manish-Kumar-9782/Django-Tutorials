from django.urls import path
from .views import task_list, add_taskList, add_task, delete_taskList, update_taskList_tasks, delete_task, update_task


urlpatterns = [
    path("", view=task_list, name='view_tasks'),
    path("add", view=add_taskList, name='add_taskList'),
    path("add_task/<int:taskListId>", view=add_task, name='add_task'),
    path("delete_taskList/<int:taskListId>",
         view=delete_taskList, name='delete_taskList'),
    path("update_taskList_tasks", view=update_taskList_tasks,
         name='update_taskList_tasks'),

    path("delete_task/<int:taskId>", view=delete_task, name="delete_task"),
    path("update_task/<int:taskId>", view=update_task, name="update_task"),

]
