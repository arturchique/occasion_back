from enum import Enum


class IssueStatus(Enum):
    ACTIVE = 'active'
    EXECUTOR_FOUND = 'found'
    DONE = 'done'
    CLOSED = 'closed'
