from django.db import models
from enumfields import EnumField
from django.contrib.auth import get_user_model

from telegram import consts
from directory import models as directory_models

User = get_user_model()


class TelegramInviteLink(models.Model):
    link = models.CharField(max_length=128)
    channel = models.ForeignKey(
        to='TelegramChannel',
        on_delete=models.PROTECT,
        related_name='telegram_invite_links'
    )
    user = models.ForeignKey(
        to=User,
        related_name='telegram_invite_links',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    status = EnumField(
        enum=consts.InviteLinkStatus,
        max_length=16,
        default=consts.InviteLinkStatus.ACTIVE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('channel', 'user')

    def __str__(self):
        return self.link

    def mark_used(self):
        self.status = consts.InviteLinkStatus.USED
        self.save(update_fields=('status', ))

    def mark_revoked(self):
        self.status = consts.InviteLinkStatus.REVOKED
        self.save(update_fields=('status', ))


class TelegramChannel(models.Model):
    channel_id = models.BigIntegerField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)
    from_region = models.ForeignKey(
        to=directory_models.Region,
        on_delete=models.PROTECT,
        related_name='directions_to',
        null=True,
        blank=True
    )
    to_region = models.ForeignKey(
        to=directory_models.Region,
        on_delete=models.PROTECT,
        related_name='directions_from',
        null=True,
        blank=True
    )
    members = models.ManyToManyField(
        to=User,
        related_name='channels',
    )

    class Meta:
        unique_together = ('from_region', 'to_region')

    def __str__(self):
        return self.name
