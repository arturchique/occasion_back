from django.db import models
from enumfields import EnumField
from django.contrib.auth import get_user_model


from telegram import models as telegram_models
from occasion_api import consts

User = get_user_model()


class Issue(models.Model):
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=3800, null=True, blank=True)  # because 4096 is max tg message length
    expected_date = models.DateField()
    status = EnumField(
        enum=consts.IssueStatus,
        max_length=16,
        default=consts.IssueStatus.ACTIVE
    )
    creator = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='issues_created'
    )
    executor = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='issues_executed',
        null=True,
        blank=True
    )
    channel = models.ForeignKey(
        to=telegram_models.TelegramChannel,
        on_delete=models.PROTECT,
        related_name='issues'
    )


class DeliveryItem(models.Model):
    name = models.CharField(max_length=128)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    issue = models.ForeignKey(
        to=Issue,
        on_delete=models.CASCADE,
        related_name='items'
    )
