from django.contrib import admin
from perangkat.models import *

# Register your models here.
class perangkatAdmin (admin.ModelAdmin):
    list_display = ['nama', 'vendor']
    list_filter = ()
    search_fields = ['nama', 'vendor']
    list_per_page = 25

admin.site.register(perangkat, perangkatAdmin)

