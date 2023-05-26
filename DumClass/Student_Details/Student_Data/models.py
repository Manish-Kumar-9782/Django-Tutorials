from django.db import models
from django.utils import timezone

#Create your models here.

class Student_Information(models.Model):

    student_Name = models.CharField(max_length=20)
    student_FatherName = models.CharField(max_length=20)
    student_City = models.CharField(max_length=20)
    student_Class = models.IntegerField()
    student_MobileNumber = models.IntegerField()
    regDate = models.DateTimeField(auto_now_add=timezone.now)
    updateDate = models.DateTimeField(auto_now=timezone.now)