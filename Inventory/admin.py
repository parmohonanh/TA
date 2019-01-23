from django.utils.html import format_html

from django.contrib import admin
from Inventory.models import *
from django.utils.safestring import mark_safe


class DeviceAdmin (admin.ModelAdmin):
    list_display = ['hostname', 'vendor','address','Action']
    list_filter = ()
    search_fields = ['hostname', 'vendor','address']
    list_per_page = 25

    def Action(self, obj):
       return format_html('<a id="run_action">PING</a>', obj.id)


admin.site.register(Device, DeviceAdmin)