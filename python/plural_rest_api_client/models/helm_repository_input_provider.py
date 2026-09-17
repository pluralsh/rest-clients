from enum import StrEnum


class HelmRepositoryInputProvider(StrEnum):
    AWS = "aws"
    AZURE = "azure"
    BASIC = "basic"
    BEARER = "bearer"
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
