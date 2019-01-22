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
        return format_html('<a class="btn" href="/admin/Configure/model/{}/run/">Run</a>', obj.id)


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
