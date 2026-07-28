import logging
from src.config import APP_NAME, LOG_LEVEL

def setup_logger(name: str = APP_NAME) -> logging.Logger:
    """
    Configura e retorna um logger padronizado para o projeto.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(LOG_LEVEL)

    return logger


def format_currency(value: float) -> str:
    """
    Formata um valor numérico como moeda brasileira (R$).
    """

    try:
        return (
            "R$ "
            + f"{float(value):,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    except (TypeError, ValueError):
        return "R$ 0,00"


def format_percentage(value: float, decimals: int = 2) -> str:
    """
    Formata um valor numérico como percentual, utilizando vírgula
    como separador decimal.
    """

    try:
        return f"{float(value):.{decimals}f}".replace(".", ",") + "%"
    except (TypeError, ValueError):
        return "0,00%"


def safe_get(data: dict, key: str, default=None):
    """
    Retorna um valor de um dicionário de forma segura, evitando
    exceções quando a chave não existe ou o dado é None.
    """

    if not isinstance(data, dict):
        return default

    value = data.get(key, default)

    return value if value is not None else default


def truncate_text(text: str, max_length: int = 200) -> str:
    """
    Trunca um texto longo adicionando reticências, útil para logs e
    mensagens de depuração.
    """

    if not text:
        return ""

    return text if len(text) <= max_length else text[:max_length].rstrip() + "..."