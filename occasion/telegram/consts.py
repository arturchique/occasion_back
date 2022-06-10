from enum import Enum


class InviteLinkStatus(Enum):
    REVOKED = 'revoked'
    ACTIVE = 'active'
    USED = 'used'

    def __str__(self):
        return self.value
