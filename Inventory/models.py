from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Device(models.Model):
    hostname = models.CharField(max_length=100, null=True)
    vendor = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.hostname
        return self.address

