from enum import StrEnum


class StackStatus(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    PENDING_APPROVAL = "pending_approval"
    QUEUED = "queued"
    RUNNING = "running"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
