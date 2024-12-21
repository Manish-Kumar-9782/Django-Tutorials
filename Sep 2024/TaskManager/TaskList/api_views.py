from django.http import JsonResponse
from .models import TaskList, Task
import json


def to_json(query_set):
    return list(query_set.values())


def get_task_lists(request):

    task_lists = TaskList.objects.all()
    json_format = to_json(task_lists)
    return JsonResponse(json_format, safe=False)


def api_add_task(request):

    if request.method == "POST":

        try:
            print("before load: ", request.body, type(request.body))
            data = json.loads(request.body)
            print("After load: ", data, type(data))

            text = data.get("text")
            taskListId = data.get("taskList")

            taskList = TaskList.objects.get(id=taskListId)
            task = Task(text=text, task_list=taskList)
            task.save()

            return JsonResponse({"success:": "Task Successfully added",
                                "data": {"text": text, "taskListId": taskListId, 'taskId': task.id},
                                 "html": {}
                                 }, safe=False, status=201)

        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=500)


def api_delete_task(request):

    if request.method == "POST":

        try:
            print("before load: ", request.body, type(request.body))
            data = json.loads(request.body)
            print("After load: ", data, type(data))

            taskId = data.get("taskId")

            task = Task.objects.get(pk=taskId)
            task.delete()

            return JsonResponse({"status": "success",
                                 "message:": "Task Successfully Deleted",
                                "data": {"taskId": taskId}
                                 }, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=500)


def api_update_task(request):

    if request.method == "POST":

        try:
            print("before load: ", request.body, type(request.body))
            data = json.loads(request.body)
            print("After load: ", data, type(data))

            taskId = data.get("taskId")
            content = data.get("update")

            task = Task.objects.get(pk=taskId)

            # ============= updating content ============= #
            if "isCompleted" in content.keys():
                task.isCompleted = content['isCompleted']

            if "text" in content.keys():
                task.text = content['text']

            # ============= updating content ============= #

            task.save()

            return JsonResponse({"status": "success",
                                 "message:": "Task Successfully Updated..",
                                "data": {"taskId": taskId, "update": content}
                                 }, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=500)
