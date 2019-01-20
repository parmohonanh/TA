from django.conf.urls import url

from django.contrib import admin
from Inventory.models import *
from django.utils.safestring import mark_safe
import subprocess as sp


class DeviceAdmin (admin.ModelAdmin):
    list_display = ['hostname', 'vendor','address','Action']
    list_filter = ()
    search_fields = ['hostname', 'vendor','address']
    list_per_page = 25

    def Action(self, obj):
        return mark_safe('<input type="button" value="PING" name="ping_action">')


    # def ipcheck(self):
    #     status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
    #     if status == 0:
    #          print("System " + str(pop) + " is UP !")
    #     else:
    #          print("System " + str(pop) + " is DOWN !")

admin.site.register(Device, DeviceAdmin)