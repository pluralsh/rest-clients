from enum import StrEnum


class AgentRunStatus(StrEnum):
    BABYSITTING = "babysitting"
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    PENDING_APPROVAL = "pending_approval"
    RUNNING = "running"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
