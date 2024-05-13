from django.db import models

# Create your models here.


class Employee(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
