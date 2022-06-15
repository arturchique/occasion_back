import abc
import datetime
from typing import Optional, Dict, Any

import celery
from django.db import transaction

from basics import models, consts, helpers, exceptions


class BaseExternalService(celery.Task, abc.ABC):
    """Base user external service."""

    POSTPONED = False

    name: str
    error_message: str = 'External error.'
    priority: int = 0

    def __init__(self, eta: Optional[datetime.datetime] = None):
        self.eta = eta

    @property
    def external_on(self) -> bool:
        return True

    def delay(self, *args, **kwargs):
        return self.apply_async(args=args, kwargs=kwargs, eta=self.eta)

    def handle(
        self,
        meta: Optional[Dict[str, Any]] = None,
        raise_exception: bool = False,
        sync: bool = False
    ) -> None:
        """
        Calls user external service.
        Args:
            meta (Optional[Dict[str, Any]]):
            raise_exception (bool):
            sync (bool):
        Returns:
            None
        Raises:
            ExternalError: if raise_exception is True and external service call result is False.
        """

        log = models.ExternalServicesLog.objects.create(
            meta=meta,
            external_on=self.external_on,
            external_service_name=self.name,
            status=consts.ExternalServicesLogStatus.RECEIVED
        )

        if self.POSTPONED:
            log.update_status(consts.ExternalServicesLogStatus.POSTPONED)
            return

        if not sync:
            transaction.on_commit(
                lambda: helpers.call_celery_task(
                    self,
                    log_id=log.id,
                    meta=meta,
                    raise_exception=raise_exception
                )
            )
        else:
            self.run(
                log_id=log.id,
                meta=meta,
                raise_exception=raise_exception
            )

    def run(
        self,
        log_id: int,
        meta: Optional[Dict[str, Any]] = None,
        raise_exception: bool = False
    ) -> None:
        log = models.ExternalServicesLog.objects.get(id=log_id)
        log.update_status(consts.ExternalServicesLogStatus.RUNNING)

        return self._run(log=log, meta=meta, raise_exception=raise_exception)

    def _run(
        self,
        log: models.ExternalServicesLog,
        meta: Optional[Dict[str, Any]] = None,
        raise_exception: bool = False
    ) -> None:
        """
        Calls user external service.
        Args:
            meta (Optional[Dict[str, Any]]):
            raise_exception (bool):
        Returns:
            bool: is successful.
        Raises:
            ExternalError: if raise_exception is True and external service call result is False.
        """
        self.meta = meta if meta is not None else {}

        if not self.external_on or not self.validation():
            log.update_status(consts.ExternalServicesLogStatus.VALIDATE_ERROR)
            raise exceptions.ExternalError(self.error_message)

        log.update_status(consts.ExternalServicesLogStatus.VALIDATED)

        data = self.pre_serialize()
        log.update_status(consts.ExternalServicesLogStatus.SERIALIZED)

        result = self.execute(data=data)

        if raise_exception and not result:
            log.update_status(consts.ExternalServicesLogStatus.ERROR)
            raise exceptions.ExternalError(self.error_message)

        log.executed(result)

    def validation(self) -> bool:
        """
        Validates data.
        Returns:
            bool: is valid.
        """
        return True

    @abc.abstractmethod
    def pre_serialize(self) -> Dict[str, Any]:
        """
        Serialize data for call external service.
        Returns:
            Dict[str, Any]: serialize data.
        """
        pass

    @abc.abstractmethod
    def execute(self, data: Dict[str, Any]) -> bool:
        """
        Calls external service.
        Args:
            data:
        Returns:
            bool: external service call result.
        """
        pass


