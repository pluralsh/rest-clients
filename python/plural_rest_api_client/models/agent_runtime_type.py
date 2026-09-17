from enum import StrEnum


class AgentRuntimeType(StrEnum):
    CLAUDE = "claude"
    CODEX = "codex"
    CUSTOM = "custom"
    GEMINI = "gemini"
    OPENCODE = "opencode"
    PI = "pi"

    def __str__(self) -> str:
        return str(self.value)
