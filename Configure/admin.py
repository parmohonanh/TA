from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.utils.safestring import mark_safe
from django.contrib import admin
from Configure.models import *


class CommandAdmin(admin.ModelAdmin):
    list_display = ['Title', 'command']
    list_filter = ()
    search_fields = ['Title', 'command']
    list_per_page = 25


admin.site.register(Command, CommandAdmin)


class AutomationAdmin(admin.ModelAdmin):
    list_display = ['id','hostname', 'address','password', 'Job','Action']
    list_filter = ()
    search_fields = ['hostname', 'address', 'action']
    list_per_page = 25

    def Action(self, obj):
        return mark_safe("<a href=''>Run</a>")

def hostname(obj):
    return "\n".join([p.hostname for p in obj.devices.all()])


def Job(obj):
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
def pre_save(sender, instance, **kwargs):
    import paramiko
    import time

    ip_ok = Automation.objects.values_list('device__address',flat=True)
    print(ip_ok)
    uname = Automation.objects.values_list('device__username',flat=True)
    print(uname)
    pswd = Automation.objects.values_list('device__password',flat=True)
    print(pswd)
    cmmnd = Command.objects.values_list('automation__command__command',flat=True)
    print(cmmnd)
    ven = Automation.objects.values_list('device__vendor',flat=True)
    print(ven)
    try:
        for ip in ip_ok:
            print(ip)
            ssh_client = paramiko.SSHClient()
            print('bbbb')
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print('cccc')
            ssh_client.connect(hostname=ip, username=uname, password=pswd)
            print("Sukses Login ke {}".format(ip))
            for config in cmmnd:
                print(config)
                ssh_client.exec_command(config)
                time.sleep(1)
            print("Sukses Konfigurasi {}\n".format(ip))

    except:
        print("aaa")


admin.site.register(Automation, AutomationAdmin)
