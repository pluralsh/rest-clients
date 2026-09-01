from enum import StrEnum


class AgentRunMode(StrEnum):
    ANALYZE = "analyze"
    REVIEW = "review"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
