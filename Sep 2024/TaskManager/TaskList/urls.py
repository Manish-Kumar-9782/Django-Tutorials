from django.urls import path
from .views import task_list, add_task


urlpatterns = [
    path("", view=task_list, name='view_tasks'),
    path("add", view=add_task, name='add_task')
]
