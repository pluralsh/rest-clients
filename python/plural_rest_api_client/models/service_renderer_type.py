from enum import StrEnum


class ServiceRendererType(StrEnum):
    AUTO = "auto"
    HELM = "helm"
    KUSTOMIZE = "kustomize"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
