from enum import Enum


class AgentRunStatus(str, Enum):
    BABYSITTING = "babysitting"
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    PENDING_APPROVAL = "pending_approval"
    RUNNING = "running"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
