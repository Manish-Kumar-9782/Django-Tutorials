from django.db import models

# Create your models here.


class Student(models.Model):

    Name = models.CharField(max_length=30, default="")
    Std = models.CharField(max_length=10, default="")
    RollNo = models.CharField(max_length=10, default="")
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=50)
    Address = models.CharField(max_length=100)
    Stream = models.CharField(max_length=30)
