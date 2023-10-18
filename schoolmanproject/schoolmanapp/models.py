from django.db import models



# Create your models here.

class Student_Data_Row(models.Model):
    row_number = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)
