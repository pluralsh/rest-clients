from enum import StrEnum


class AgentSessionType(StrEnum):
    CHAT = "chat"
    CONFIGURE = "configure"
    KUBERNETES = "kubernetes"
    MANIFESTS = "manifests"
    PROVISIONING = "provisioning"
    RESEARCH = "research"
    SEARCH = "search"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
