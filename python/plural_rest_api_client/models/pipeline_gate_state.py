from enum import StrEnum


class PipelineGateState(StrEnum):
    CLOSED = "closed"
    OPEN = "open"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
