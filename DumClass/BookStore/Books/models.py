from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField()
    regDate = models.DateTimeField(auto_now_add=timezone.now)
    updateDate = models.DateTimeField(auto_now=timezone.now)