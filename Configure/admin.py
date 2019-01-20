from django.db.models.signals import pre_save
from django.contrib import admin
from Configure.models import *
from django.dispatch import receiver


class CommandAdmin(admin.ModelAdmin):
    list_display = ['Title', 'command']
    list_filter = ()
    search_fields = ['Title', 'command']
    list_per_page = 25


admin.site.register(Command, CommandAdmin)


class AutomationAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'address', 'action']
    list_filter = ()
    search_fields = ['hostname', 'address', 'action']
    list_per_page = 25


def hostname(obj):
    return "\n".join([p.hostname for p in obj.devices.all()])


def action(obj):
    return "\n".join([p.Title for p in obj.command.all()])


def action2(obj):
    return "\n".join([p.command for p in obj.command.all()])


def address(obj):
    return "\n".join([p.address for p in obj.devices.all()])


def vendor(obj):
    return "\n".join([p.vendor for p in obj.devices.all()])


def username(obj):
    return "\n".join([p.username for p in obj.devices.all()])


def password(obj):
    return "\n".join([p.password for p in obj.devices.all()])


@receiver(pre_save, sender=Automation)
def pre_save_person(sender, instance, **kwargs):
    import paramiko
    import time

    try:
        for ip in address:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip, username=username, password=password[0])
            print("Sukses Login ke {}".format(ip))
            for config in action2:
                ssh_client.exec_command(config)
                time.sleep(1)
            print("Sukses Konfigurasi {}\n".format(ip))

    except:
        print("")


admin.site.register(Automation, AutomationAdmin)
