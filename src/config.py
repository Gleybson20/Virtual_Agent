from pathlib import Path
from dotenv import load_dotenv
import os

ROOT_DIR = Path(__file__).resolve().parent.parent

load_dotenv(ROOT_DIR / ".env")

DATA_DIR = ROOT_DIR / "data"

PROMPTS_DIR = ROOT_DIR / "prompts"

SRC_DIR = ROOT_DIR / "src"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")

TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))

MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))

DEFAULT_CLIENT_ID = int(
    os.getenv("DEFAULT_CLIENT_ID", "1")
)

LOG_LEVEL = "INFO"

PROMPT_FILES = {
    "system": "system_prompt.md",
    "guardrails": "guardrails.md",
    "few_shots": "few_shots.md",
    "context": "context_template.md",
    "output": "output_format.md",
}

MAX_QUESTION_LENGTH = 3000

MIN_QUESTION_LENGTH = 2

APP_NAME = "Advisor Invest"

APP_VERSION = "1.0.0"

APP_AUTHOR = "Gleybson Ricardo"

def validate_configuration() -> None:
    """
    Verifica se as configurações essenciais foram carregadas.
    """

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY não encontrada. "
            "Configure a variável no arquivo .env."
        )