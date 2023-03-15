from django.db import models

# Create your models here.


class Student(models.Model):

    Name = models.CharField(max_length=30, default="")
    Class = models.CharField(max_length=5, default="")
    Section = models.CharField(max_length=30, default="")
    Address = models.CharField(max_length=50, default="")
    MobileNo = models.CharField(max_length=10, default="")

    def __str__(self) -> str:
        return self.Name
