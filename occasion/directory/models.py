from django.db import models


class Region(models.Model):
    name = models.CharField(
        max_length=62,  # tg channel name has 128 max len, and we have f'{region} -> {region}' as channel name
        unique=True
    )
    country = models.CharField(max_length=64, null=True, blank=True)  # TODO create choices
