from enum import StrEnum


class ListGitRepositoriesHealth(StrEnum):
    FAILED = "failed"
    PULLABLE = "pullable"

    def __str__(self) -> str:
        return str(self.value)
