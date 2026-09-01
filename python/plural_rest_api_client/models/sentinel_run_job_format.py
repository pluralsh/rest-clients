from enum import StrEnum


class SentinelRunJobFormat(StrEnum):
    JUNIT = "junit"
    PLAINTEXT = "plaintext"

    def __str__(self) -> str:
        return str(self.value)
