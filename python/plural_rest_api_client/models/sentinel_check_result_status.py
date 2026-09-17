from enum import StrEnum


class SentinelCheckResultStatus(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
