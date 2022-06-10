from django.contrib import admin

from occasion_bot import models
from basics.admin import BaseVerboseModelAdmin


class IssueAdmin(BaseVerboseModelAdmin):
    # TODO write tomorrow)))
    pass


class DeliveryItemAdmin(BaseVerboseModelAdmin):
    # TODO write tomorrow)))
    pass


# Registrations
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.DeliveryItem, DeliveryItemAdmin)
