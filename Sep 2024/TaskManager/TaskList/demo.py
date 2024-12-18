from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Task, TaskList
from django.core.serializers import serialize
import json


@require_http_methods(["GET"])
def get_all_tasklists(request):
    try:
        tasklists = TaskList.objects.all()
        response_data = []

        for tasklist in tasklists:
            tasks = Task.objects.filter(task_list=tasklist)
            task_data = []
            for task in tasks:
                task_data.append({
                    "id": task.id,
                    "task_name": task.task_name,
                    "task_description": task.task_description,
                    "due_date": task.due_date
                })
            response_data.append({
                "id": tasklist.id,
                "name": tasklist.name,
                "tasks": task_data
            })

        return JsonResponse(response_data, safe=False, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
