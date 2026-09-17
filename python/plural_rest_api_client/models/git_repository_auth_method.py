from enum import StrEnum


class GitRepositoryAuthMethod(StrEnum):
    BASIC = "basic"
    SSH = "ssh"

    def __str__(self) -> str:
        return str(self.value)
