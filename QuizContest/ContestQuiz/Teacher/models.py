from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):

    Name = models.CharField(max_length=30, default='')
    Subject = models.CharField(max_length=30, default='')
    Dob = models.DateField(default=timezone.now)
    Address = models.CharField(max_length=50, default='')
    MobileNo = models.CharField(max_length=10, default='')
    UserAccount = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.Name}"
