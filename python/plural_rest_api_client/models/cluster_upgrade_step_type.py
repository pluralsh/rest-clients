from enum import StrEnum


class ClusterUpgradeStepType(StrEnum):
    ADDON = "addon"
    CLOUD_ADDON = "cloud_addon"
    INFRASTRUCTURE = "infrastructure"

    def __str__(self) -> str:
        return str(self.value)
