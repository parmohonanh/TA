from django.utils.html import format_html

from django.contrib import admin
from Inventory.models import *


class DeviceAdmin (admin.ModelAdmin):
    list_display = ['hostname', 'vendor','address']
    list_filter = ()
    search_fields = ['hostname', 'vendor','address']
    list_per_page = 25


admin.site.register(Device, DeviceAdmin)