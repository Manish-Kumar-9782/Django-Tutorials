from django.db import models

# Create your models here.


class Teacher(models.Model):

    Name = models.CharField(max_length=30)
    Subject = models.CharField(max_length=30)
    Dob = models.DateField()
    Address = models.CharField(max_length=50)
    MobileNo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.Name}"
