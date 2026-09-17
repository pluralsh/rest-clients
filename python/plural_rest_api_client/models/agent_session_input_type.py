from enum import StrEnum


class AgentSessionInputType(StrEnum):
    KUBERNETES = "kubernetes"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
