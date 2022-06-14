from django.contrib import admin

from users import models
from basics.base.admin import BaseVerboseModelAdmin


class UserAdmin(BaseVerboseModelAdmin):
    list_display = ('id', 'tg_id', 'tg_username', 'first_name', 'last_name', )
    search_fields = ('id', 'tg_id', 'tg_username', 'first_name', 'last_name', )
    readonly_fields = ('password', 'tg_id', 'tg_username', )


# Registrations
admin.site.register(models.User, UserAdmin)
