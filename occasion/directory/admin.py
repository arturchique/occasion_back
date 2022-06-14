from django.contrib import admin

from directory import models
from basics.base.admin import BaseVerboseModelAdmin


class RegionAdmin(BaseVerboseModelAdmin):
    list_display = ('id', 'name', 'country', )
    list_filter = ('country', )
    search_fields = ('id', 'name', )


# Registrations
admin.site.register(models.Region, RegionAdmin)
