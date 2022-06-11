from django.contrib import admin

from occasion_bot import models
from basics.admin import BaseVerboseModelAdmin


class IssueAdmin(BaseVerboseModelAdmin):
    list_display = (
        'id',
        'summary',
        'description',
        'expected_date',
        'status',
        'creator',
        'executor',
        'channel'
    )
    list_filter = ('channel', 'status', 'to_region',)
    search_fields = (
        'summary',
        'description',
        'channel',
        'creator',
        'executor',
        'channel__from_region',
        'channel__to_region',
    )
    readonly_fields = ('creator', )


class DeliveryItemAdmin(BaseVerboseModelAdmin):
    list_display = ('name', 'weight', 'width', 'height', 'depth', 'issue', )


# Registrations
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.DeliveryItem, DeliveryItemAdmin)
