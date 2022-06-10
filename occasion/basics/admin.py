from django.contrib import admin


class BaseVerboseModelAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
