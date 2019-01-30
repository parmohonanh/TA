from Inventory.models import Device
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class Command(models.Model):
    Title = models.CharField(max_length=100, null=True, unique=True)
    command = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Title


class Automation(models.Model):
    device = models.ManyToManyField(Device)
    command = models.ManyToManyField(Command)

    def hostname(self):
        return "\n".join([p.hostname for p in self.device.all()])

    def Job(self):
        return "\n".join([p.Title for p in self.command.all()])

    def action2(self):
        return "\n".join([p.command for p in self.command.all()])

    def address(self):
        return "\n".join([p.address for p in self.device.all()])

    def vendor(self):
        return "\n".join([p.vendor for p in self.device.all()])

    def username(self):
        return "\n".join([p.username for p in self.device.all()])

    def password(self):
        return "\n".join([p.password for p in self.device.all()])

    def __unicode__(self):
        return self.device

