from Inventory.models import Device
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class Command(models.Model):
    Title = models.CharField(max_length=100, null=True, unique=True)
    command = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Title


class Automation(models.Model):
    device = models.ManyToManyField(Device)
    command = models.ManyToManyField(Command)

    def run(sender, instance, **kwargs):
        import paramiko
        import time

        ip_ok = ['10.10.10.100']
        uname = ['user1']
        pswd = ['user1']
        cmnd =['ip service enable ftp']
        try:
            for ip in ip_ok:
                print(ip)
                ssh_client = paramiko.SSHClient()
                print('bbbb')
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print('cccc')
                ssh_client.connect(hostname=ip, username=uname, password=pswd)
                print(uname)
                print(pswd)
                print("Sukses Login ke {}".format(ip))
                for config in cmnd:
                    print(config)
                    ssh_client.exec_command(config)
                    time.sleep(1)
                print("Sukses Konfigurasi {}\n".format(ip))

        except:
            print("aaa")

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

