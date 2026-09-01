from enum import StrEnum


class WorkbenchBudgetUnit(StrEnum):
    DOLLAR = "dollar"
    TOKEN = "token"

    def __str__(self) -> str:
        return str(self.value)
