from enum import StrEnum


class SentinelCheckType(StrEnum):
    INTEGRATION_TEST = "integration_test"
    KUBERNETES = "kubernetes"
    LOG = "log"

    def __str__(self) -> str:
        return str(self.value)
