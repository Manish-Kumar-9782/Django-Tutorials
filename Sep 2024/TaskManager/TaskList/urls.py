from django.urls import path
from .views import task_list, add_taskList, add_task, delete_task, update_taskList_tasks


urlpatterns = [
    path("", view=task_list, name='view_tasks'),
    path("add", view=add_taskList, name='add_taskList'),
    path("add_task/<int:taskListId>", view=add_task, name='add_task'),
    path("delete_task/<int:taskListId>", view=delete_task, name='delete_task'),
    path("update_taskList_tasks", view=update_taskList_tasks,
         name='update_taskList_tasks'),
]
