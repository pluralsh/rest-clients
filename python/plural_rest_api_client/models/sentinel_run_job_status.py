from enum import StrEnum


class SentinelRunJobStatus(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
