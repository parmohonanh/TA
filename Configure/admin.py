from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import paramiko
import time
from django.conf.urls import url
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from Configure.models import *


class CommandAdmin(admin.ModelAdmin):
    list_display = ['Title', 'command']
    list_filter = ()
    search_fields = ['Title', 'command']
    list_per_page = 25


admin.site.register(Command, CommandAdmin)


class AutomationAdmin(admin.ModelAdmin):
    list_display = ['id', 'hostname', 'address', 'password', 'Job', 'automation_action']
    list_filter = ()
    search_fields = ['hostname', 'address', 'action']
    list_per_page = 25


    def automation_action(self, obj):
        return format_html('<a href="{}">RUN</a>', reverse('admin:automation-account', args=[obj.pk]))
    automation_action.short_description = 'Action'
    automation_action.allow_tag=True

    def get_urls(self):
        urls =super().get_urls()
        custom_urls = [
            url(
                r'^(?P<object_id>.+)/automation/$',
                self.admin_site.admin_view(self.run_conf),
                name='automation-account'
            )
        ]
        return custom_urls + urls

    def run_conf(self,obj,object_id):
        ip_ok = Automation.objects.filter(command__automation__device=True)
        ipip = list(ip_ok)
        print(ipip)
        uname = Automation.objects.values_list('device__hostname', flat=True)
        print(uname)
        pswd = Automation.objects.values_list('device__password', flat=True)
        print(pswd)
        cmmnd = Automation.objects.values_list('command__automation__command', flat=True)
        print(cmmnd)
        ven = Automation.objects.values_list('device__vendor', flat=True)
        print(ven)

        try:
            for ip in ip_ok:
                print(ip)
                print(cmmnd)
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

        return HttpResponseRedirect (url)

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
