from django.http import JsonResponse
from .models import TaskList, Task


def to_json(query_set):
    return list(query_set.values())


def get_task_lists(request):

    task_lists = TaskList.objects.all()
    json_format = to_json(task_lists)
    return JsonResponse(json_format, safe=False)
