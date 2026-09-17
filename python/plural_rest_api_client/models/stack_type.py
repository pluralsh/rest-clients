from enum import StrEnum


class StackType(StrEnum):
    ANSIBLE = "ansible"
    CUSTOM = "custom"
    PULUMI = "pulumi"
    TERRAFORM = "terraform"
    TERRAGRUNT = "terragrunt"

    def __str__(self) -> str:
        return str(self.value)
