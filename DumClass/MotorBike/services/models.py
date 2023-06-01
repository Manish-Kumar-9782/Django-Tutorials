from django.db import models
from django.utils import timezone
# Create your models here.


class Service(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    updated_on = models.DateTimeField(auto_now=timezone.now)
