from enum import StrEnum


class ClusterDistro(StrEnum):
    AKS = "aks"
    EKS = "eks"
    GENERIC = "generic"
    GKE = "gke"
    K3S = "k3s"
    OPENSHIFT = "openshift"
    RKE = "rke"

    def __str__(self) -> str:
        return str(self.value)
