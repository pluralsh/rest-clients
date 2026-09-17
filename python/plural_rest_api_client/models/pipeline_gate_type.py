from enum import StrEnum


class PipelineGateType(StrEnum):
    APPROVAL = "approval"
    JOB = "job"
    SENTINEL = "sentinel"
    WINDOW = "window"

    def __str__(self) -> str:
        return str(self.value)
