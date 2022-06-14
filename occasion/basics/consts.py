import enum


class ExternalServicesLogStatus(enum.Enum):
    RECEIVED = 'received'
    POSTPONED = 'postponed'
    RUNNING = 'running'
    VALIDATED = 'validated'
    SERIALIZED = 'serialized'
    EXECUTED = 'executed'
    VALIDATE_ERROR = 'validate_error'
    ERROR = 'error'

    def __str__(self):
        return self.value
