from django.db import models

# Create your models here.


class TaskList(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=15)


# first generate your migrations by following command
# --> python manage.py makemigrations TaskList

# after generating migrations we need to migrate them to database
# means we need to perform database operation
# --> python manage.py migrate TaskList
