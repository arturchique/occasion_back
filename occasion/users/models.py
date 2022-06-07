from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    tg_id = models.BigIntegerField(unique=True, blank=True, null=True, verbose_name='telegram id')
    tg_username = models.CharField(max_length=32, verbose_name='telegram username')

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return ' '.join([self.last_name, self.first_name, '({0})'.format(self.username)])

    @property
    def full_name(self):
        return self.get_full_name()
