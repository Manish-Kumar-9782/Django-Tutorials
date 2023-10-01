from django.db import models

# Create your models here.


class MyUsers(models.Model):

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
