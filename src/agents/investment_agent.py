from src.config import DEFAULT_CLIENT_ID
from src.context.context_builder import ContextBuilder
from src.context.prompt_builder import PromptBuilder
from src.LLM.provider import LLMProvider
from src.validators.input_validator import InputValidator, InputValidationError
from src.validators.response_validator import ResponseValidator
from src.services.investment_service import InvestmentService
from src.services.macro_service import MacroService
from src.services.company_analysis import CompanyAnalysisService
from src.utils.helpers import setup_logger

logger = setup_logger(__name__)


class InvestmentAgent:
    """
    Consolida todos os componentes do Advisor Invest em uma única
    interface de uso simples: `ask(cliente_id, pergunta)`.
    """

    def __init__(self):
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMProvider()

        self.input_validator = InputValidator()
        self.response_validator = ResponseValidator()

        self.investment_service = InvestmentService()
        self.macro_service = MacroService()
        self.company_service = CompanyAnalysisService()

    def ask(self, question: str, cliente_id: int = DEFAULT_CLIENT_ID) -> dict:
        """
        Processa uma pergunta do usuário e retorna a resposta gerada
        pelo agente junto com o resultado da validação de segurança.

        Retorno:
            {
                "resposta": str,
                "validacao": dict,
                "cliente_encontrado": bool,
            }
        """

        try:
            pergunta_validada = self.input_validator.validate(question)
        except InputValidationError as erro:
            logger.warning("Pergunta rejeitada na validação de entrada: %s", erro)
            return {
                "resposta": str(erro),
                "validacao": {"valido": False, "erros": [str(erro)]},
                "cliente_encontrado": False,
            }

        contexto = self.context_builder.build_context(cliente_id)
        cliente_encontrado = bool(contexto.get("perfil"))

        if not cliente_encontrado:
            logger.info(
                "Cliente %s não encontrado na Base de Conhecimento.", cliente_id
            )

        prompt = self.prompt_builder.build_prompt(contexto, pergunta_validada)

        resposta = self.llm.generate(prompt)

        validacao = self.response_validator.validate(resposta)

        if not validacao["valido"]:
            logger.warning(
                "Resposta gerada não passou em todas as validações: %s",
                validacao["erros"],
            )

        return {
            "resposta": resposta,
            "validacao": validacao,
            "cliente_encontrado": cliente_encontrado,
        }

    def analyze_portfolio(self, cliente_id: int = DEFAULT_CLIENT_ID) -> dict:
        """
        Retorna um resumo estruturado da carteira e do comportamento
        de investimento do cliente, sem depender de uma chamada ao
        LLM. Útil para dashboards ou para enriquecer o contexto de
        uma pergunta futura.
        """

        return {
            "carteira": self.investment_service.portfolio_summary(cliente_id),
            "comportamento": self.investment_service.behavior_summary(cliente_id),
            "produtos_recomendados": self.investment_service.recommend_products(
                cliente_id
            ),
        }

    def explain_macro_indicator(self, indicador: str, classe_ativo: str = "") -> str:
        """
        Retorna a explicação conceitual de um indicador
        macroeconômico e, quando informado, seu impacto sobre uma
        classe de ativo específica.
        """

        dados = self.macro_service.get_indicator(indicador)

        if not dados:
            return (
                "Não possuo fundamentação suficiente sobre esse "
                "indicador na minha base de conhecimento."
            )

        if classe_ativo:
            impacto = self.macro_service.explain_impact(indicador, classe_ativo)
            if impacto:
                return f"{dados['descricao']}\n\nImpacto: {impacto}"

        return dados["descricao"]

    def compare_companies(self, empresa_a: dict, empresa_b: dict) -> dict:
        """
        Estrutura a comparação entre duas empresas a partir dos
        indicadores financeiros informados.
        """

        return self.company_service.compare(empresa_a, empresa_b)

    def health_check(self) -> bool:
        """
        Verifica se o provedor de LLM está acessível.
        """

        return self.llm.health_check()