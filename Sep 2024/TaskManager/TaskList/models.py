from django.db import models

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=100)
    # need to convert to Choice Field
    priority = models.CharField(max_length=15, default="low")
    isCompleted = models.BooleanField(default=False)
    # applying oneToMany Relationship in b/w the Task and TaskList
    task_list = models.ForeignKey(
        'TaskList', on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.text


class TaskList(models.Model):

    title = models.CharField(max_length=50)
    # need to convert to Choice Field
    category = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add : auto fill for datetime at the time is being created
    modified = models.DateTimeField(auto_now=True)
    # auto_now: update datetime each time the object is saved
