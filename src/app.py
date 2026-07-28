from src.agents.investment_agent import InvestmentAgent
from src.config import APP_NAME, APP_VERSION, DEFAULT_CLIENT_ID, validate_configuration
from src.utils.helpers import setup_logger

logger = setup_logger(__name__)


BANNER = f"""
==================================================
 {APP_NAME} v{APP_VERSION}
 Consultor Financeiro Virtual
==================================================
Digite sua pergunta sobre investimentos, economia
ou finanças. Digite 'sair' para encerrar.
"""


def run_cli() -> None:
    """
    Executa o loop de conversa via terminal.
    """

    print(BANNER)

    try:
        validate_configuration()
    except ValueError as erro:
        print(f"Erro de configuração: {erro}")
        return

    agent = InvestmentAgent()
    cliente_id = DEFAULT_CLIENT_ID

    while True:
        pergunta = input("\nVocê: ").strip()

        if pergunta.lower() in {"sair", "exit", "quit"}:
            print(f"\n{APP_NAME}: Até logo! Bons investimentos.")
            break

        if not pergunta:
            continue

        resultado = agent.ask(pergunta, cliente_id=cliente_id)

        print(f"\n{APP_NAME}:\n{resultado['resposta']}")

        if not resultado["validacao"]["valido"]:
            logger.warning(
                "Atenção: a resposta apresentou inconsistências: %s",
                resultado["validacao"]["erros"],
            )


if __name__ == "__main__":
    run_cli()