from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone
# Create your models here.


class Student(models.Model):

    Name = models.CharField(max_length=30, default="")
    Class = models.CharField(max_length=5, default="")
    Section = models.CharField(max_length=30, default="")
    Address = models.CharField(max_length=50, default="")
    MobileNo = models.CharField(max_length=10, default="")
    Email = models.EmailField(max_length=50, default="")
    Dob = models.DateField(default=timezone.now)

    UserAccount = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.Name
