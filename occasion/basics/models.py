from enumfields import EnumField

from django.db import models
from django_cryptography import fields as crypto_fields

from basics import consts


class ExternalServicesLog(models.Model):
    external_on = models.BooleanField()
    meta = crypto_fields.PickledField(max_length=512, blank=True, null=True, verbose_name='Meta Data')
    created_dt = models.DateTimeField(auto_now_add=True)
    external_service_name = models.CharField(max_length=128, verbose_name='UserExternalService class name')
    result = models.BooleanField(default=False)
    status = EnumField(enum=consts.ExternalServicesLogStatus, max_length=50)

    def update_status(self, status: consts.ExternalServicesLogStatus):
        self.status = status
        self.save(update_fields=['status'])

    def executed(self, result: bool):
        self.status = consts.ExternalServicesLogStatus.EXECUTED
        self.result = result
        self.save(update_fields=['status', 'result'])
