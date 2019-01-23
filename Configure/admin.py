from django.conf.urls import url
from django.urls import reverse
from django.utils.html import format_html

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

    def Action(self,obj):
        return format_html('<a class="button" href="{}">Run</a>',
                           reverse('admin:Action',args=[obj.pk]),)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<Automation_id>.+)/automation/$',
                self.admin_site.admin_view(self.run),
                name='Action',
            )
        ]
        return custom_urls + urls
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
        return sender

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




admin.site.register(Automation, AutomationAdmin)
