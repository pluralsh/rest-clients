from enum import Enum


class WorkbenchJobStatus(str, Enum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    PAUSED = "paused"
    PENDING = "pending"
    RUNNING = "running"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
