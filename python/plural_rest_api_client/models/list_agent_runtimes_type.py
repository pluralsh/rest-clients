from enum import StrEnum


class ListAgentRuntimesType(StrEnum):
    CLAUDE = "claude"
    CUSTOM = "custom"
    GEMINI = "gemini"
    OPENCODE = "opencode"

    def __str__(self) -> str:
        return str(self.value)
