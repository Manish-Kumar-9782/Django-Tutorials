from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Service(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    updated_on = models.DateTimeField(auto_now=timezone.now)
    registeredBy = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="userId_registeredBy")
    lastUpdatedBy = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="UserId_lastUpdatedBy")

    def insertDetails(self, title, description, lastUpdatedBy, registeredBy=None):

        self.title = title
        self.description = description
        if registeredBy:
            self.registeredBy = registeredBy
        self.lastUpdatedBy = lastUpdatedBy
        self.save()


class Parts(models.Model):

    name = models.CharField(max_length=30)
    price = models.IntegerField()
    company = models.CharField(max_length=20)

    created_on = models.DateTimeField(auto_now_add=timezone.now)
    updated_on = models.DateTimeField(auto_now=timezone.now)
    registeredBy = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="part_registeredBy")
    lastUpdatedBy = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="part_lastUpdatedBy")

    def insertDetails(self, name, price, company, user, initial=False):

        self.name = name
        self.price = price
        self.company = company
        if initial:
            self.registeredBy = user
        self.lastUpdatedBy = user

        self.save()
