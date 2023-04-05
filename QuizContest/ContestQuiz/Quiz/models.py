from django.db import models


class Options(models.TextChoices):
    NONE = 'None', "None",
    OPTION1 = "1", "Option1"
    OPTION2 = "2", "Option2"
    OPTION3 = "3", "Option3"
    OPTION4 = "4", "Option4"

# Create your models here.


class Subject(models.Model):
    Subject = models.CharField(max_length=30)


class Question(models.Model):

    Subject = models.ForeignKey(Subject)
    Question = models.TextField(max_length=200)
    Option1 = models.CharField(max_length=50)
    Option2 = models.CharField(max_length=50)
    Option3 = models.CharField(max_length=50)
    Option4 = models.CharField(max_length=50)
    CorrectOption = models.CharField(
        max_length=50, default=Options.NONE, choices=Options.choices)
