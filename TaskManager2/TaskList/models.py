from django.db import models

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=100)
    isCompleted = models.BooleanField(default=False)
    priority = models.CharField(max_length=15, default="low")
    task_list = models.ForeignKey(
        'TaskList', on_delete=models.CASCADE, related_name="tasks")

# A Single TaskList object can have multiple Task object's
# oneToMany relation.


class TaskList(models.Model):

    class StatusChoices(models.TextChoices):
        ACTIVE = "active", "Active"
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"
        INIT = "init", "Init"

    class PriorityChoices(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"

    title = models.CharField(max_length=50)
    category = models.CharField(max_length=15)

    # adding priority and status with Choice list
    status = models.CharField(
        max_length=10, default=StatusChoices.INIT,  choices=StatusChoices.choices)

    priority = models.CharField(
        max_length=10, default=PriorityChoices.LOW, choices=PriorityChoices.choices)

    # now we will add few more fields
    # a field to store time at which taskList created.
    created = models.DateTimeField(auto_now_add=True)
    # a filed to store time at which taskList last modified.
    lastModify = models.DateTimeField(auto_now=True)


# Whenever you create you models or update models
# first generate your migrations by following command
# --> python manage.py makemigrations TaskList

# after generating migrations we need to migrate them to database
# means we need to perform database operation
# --> python manage.py migrate TaskList
