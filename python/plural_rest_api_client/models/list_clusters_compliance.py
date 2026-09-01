from enum import StrEnum


class ListClustersCompliance(StrEnum):
    COMPLIANT = "compliant"
    LATEST = "latest"
    OUTDATED = "outdated"

    def __str__(self) -> str:
        return str(self.value)
