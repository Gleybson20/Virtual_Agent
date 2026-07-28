from src.data_loader.perfil_loader import PerfilLoader
from src.data_loader.produtos_loader import ProdutosLoader
from src.data_loader.transacoes_loader import TransacoesLoader
from src.context.context_builder import ContextBuilder


class InvestmentService:
    """
    Centraliza regras de negócio sobre suitability, carteira e
    recomendação de produtos financeiros.
    """

    def __init__(self):
        self.perfil_loader = PerfilLoader()
        self.produtos_loader = ProdutosLoader()
        self.transacoes_loader = TransacoesLoader()
        self.context_builder = ContextBuilder()

    def get_investor_profile(self, cliente_id: int) -> dict:
        """
        Retorna o perfil cadastral do investidor.
        """

        return self.perfil_loader.get_by_id(cliente_id)

    def is_suitable(self, cliente_id: int, produto_id: int) -> bool:
        """
        Verifica se um produto financeiro é compatível com o perfil
        de risco declarado do investidor (suitability).
        """

        perfil = self.get_investor_profile(cliente_id)
        produto = self.produtos_loader.get_by_id(produto_id)

        if not perfil or not produto:
            return False

        perfil_risco = perfil.get("perfil", "").strip().lower()
        perfis_recomendados = [
            p.strip().lower() for p in produto.get("perfil_recomendado", [])
        ]

        return perfil_risco in perfis_recomendados

    def recommend_products(self, cliente_id: int) -> list[dict]:
        """
        Retorna a lista de produtos financeiros compatíveis com o
        perfil de risco do investidor.

        Caso o cliente não possua perfil cadastrado, retorna uma
        lista vazia, para que o agente informe a ausência de dados em
        vez de recomendar produtos sem fundamentação.
        """

        perfil = self.get_investor_profile(cliente_id)

        if not perfil:
            return []

        return self.produtos_loader.get_recommended_for_profile(
            perfil.get("perfil", "")
        )

    def portfolio_summary(self, cliente_id: int) -> dict:
        """
        Resume a carteira atual do cliente: valor total investido,
        valor atual, rentabilidade média ponderada e alocação por
        categoria.
        """

        carteira = self.context_builder.load_portfolio(cliente_id)

        if not carteira:
            return {
                "valor_investido_total": 0.0,
                "valor_atual_total": 0.0,
                "rentabilidade_percentual": 0.0,
                "alocacao_por_categoria": {},
            }

        valor_investido_total = sum(item["valor_investido"] for item in carteira)
        valor_atual_total = sum(item["valor_atual"] for item in carteira)

        rentabilidade_percentual = (
            round(
                (
                    (valor_atual_total - valor_investido_total)
                    / valor_investido_total
                )
                * 100,
                2,
            )
            if valor_investido_total
            else 0.0
        )

        alocacao_por_categoria: dict[str, float] = {}
        for item in carteira:
            categoria = item.get("categoria", "Outros")
            alocacao_por_categoria[categoria] = alocacao_por_categoria.get(
                categoria, 0.0
            ) + item.get("valor_atual", 0.0)

        return {
            "valor_investido_total": round(valor_investido_total, 2),
            "valor_atual_total": round(valor_atual_total, 2),
            "rentabilidade_percentual": rentabilidade_percentual,
            "alocacao_por_categoria": {
                categoria: round(valor, 2)
                for categoria, valor in alocacao_por_categoria.items()
            },
        }

    def behavior_summary(self, cliente_id: int) -> dict:
        """
        Retorna um resumo do comportamento de investimento do cliente
        a partir do histórico de transações.
        """

        return self.transacoes_loader.summary_by_client(cliente_id)

    def build_knowledge_snippet(self, cliente_id: int) -> str:
        """
        Monta um trecho textual com recomendações compatíveis com o
        perfil do investidor, pronto para ser incorporado ao contexto
        enviado ao LLM.
        """

        recomendados = self.recommend_products(cliente_id)

        if not recomendados:
            return (
                "Não há dados suficientes de perfil para recomendar "
                "produtos financeiros compatíveis."
            )

        linhas = ["Produtos compatíveis com o perfil do investidor:"]
        for produto in recomendados:
            linhas.append(
                f"- {produto['nome']} ({produto['categoria']}, "
                f"risco {produto['risco']}): {produto['descricao']}"
            )

        return "\n".join(linhas)