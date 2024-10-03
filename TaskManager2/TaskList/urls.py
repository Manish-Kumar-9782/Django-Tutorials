from django.urls import path

from .views import task_list, add_task

urlpatterns = [
    path("", view=task_list, name="show_task_lists"),
    path("add", view=add_task, name="add_task_list")
]
