from enum import StrEnum


class ServiceStatus(StrEnum):
    FAILED = "failed"
    HEALTHY = "healthy"
    PAUSED = "paused"
    STALE = "stale"
    SYNCED = "synced"

    def __str__(self) -> str:
        return str(self.value)
