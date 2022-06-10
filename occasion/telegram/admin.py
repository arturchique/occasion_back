from django.contrib import admin

from telegram import models
from basics.admin import BaseVerboseModelAdmin


class TelegramChannelAdmin(BaseVerboseModelAdmin):
    list_display = ('tg_id', 'name', 'is_active', 'from_region', 'to_region', )
    list_filter = ('is_active', 'from_region', 'to_region', )
    search_fields = ('tg_id', 'name', 'from_region', 'to_region', )
    readonly_fields = ('tg_id', 'tg_id', 'from_region', 'to_region')


class TelegramInviteLinkAdmin(BaseVerboseModelAdmin):
    list_display = ('id', 'link', 'channel', 'user', 'status', 'created', )
    list_filter = ('channel', 'status', )
    search_fields = (
        'link',
        'channel__tg_id',
        'channel__name',
        'user__tg_id',
        'user__tg_username',
        'user__first_name',
        'user__last_name',
        'status',
        'created',
    )
    readonly_fields = ('link', 'channel', 'user', 'created')


# Registrations
admin.site.register(models.TelegramChannel, TelegramChannelAdmin)
admin.site.register(models.TelegramInviteLink, TelegramInviteLinkAdmin)
