import celery

from occasion import settings


def call_celery_task(celery_task: celery.Task, *args, **kwargs):
    if settings.USE_CELERY:
        return celery_task.delay(*args, **kwargs)
    else:
        return celery_task.run(*args, **kwargs)