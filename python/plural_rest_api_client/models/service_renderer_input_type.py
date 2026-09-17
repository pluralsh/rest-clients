from enum import StrEnum


class ServiceRendererInputType(StrEnum):
    AUTO = "auto"
    HELM = "helm"
    KUSTOMIZE = "kustomize"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
