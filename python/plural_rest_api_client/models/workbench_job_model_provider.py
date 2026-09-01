from enum import StrEnum


class WorkbenchJobModelProvider(StrEnum):
    ANTHROPIC = "anthropic"
    AZURE = "azure"
    BEDROCK = "bedrock"
    OLLAMA = "ollama"
    OPENAI = "openai"
    OPENAI_COMPATIBLE = "openai_compatible"
    VERTEX = "vertex"
    XAI = "xai"

    def __str__(self) -> str:
        return str(self.value)
