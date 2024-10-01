from django.db import models

# Create your models here.


class TaskList(models.Model):

    title = models.CharField(max_length=50)
    category = models.CharField(max_length=15)
