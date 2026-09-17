from enum import StrEnum


class GitRepositoryHealth(StrEnum):
    FAILED = "failed"
    PULLABLE = "pullable"

    def __str__(self) -> str:
        return str(self.value)
