from pathlib import Path
import pandas as pd
from src.config import DATA_DIR

class TransacoesLoader:
    """
    Carrega e consulta o histórico de movimentações financeiras do cliente.
    """

    def __init__(self, data_path: Path = DATA_DIR):
        self.file = Path(data_path) / "transacoes.csv"

    def load_all(self) -> pd.DataFrame:
        """
        Retorna todas as transações cadastradas na base.
        """

        if not self.file.exists():
            return pd.DataFrame()

        return pd.read_csv(self.file)

    def get_by_client(self, cliente_id: int) -> list[dict]:
        """
        Retorna as transações de um cliente específico, ordenadas
        da mais antiga para a mais recente.
        """

        df = self.load_all()

        if df.empty:
            return []

        cliente_df = df[df["cliente_id"] == cliente_id].sort_values("data")

        return cliente_df.to_dict(orient="records")

    def summary_by_client(self, cliente_id: int) -> dict:
        """
        Calcula um resumo do comportamento financeiro do cliente:
        quantidade de operações, ticket médio, total investido e
        produtos mais movimentados.

        Esse resumo apoia o agente a compreender hábitos do investidor
        sem a necessidade de reprocessar o histórico completo a cada
        pergunta.
        """

        transacoes = self.get_by_client(cliente_id)

        if not transacoes:
            return {
                "quantidade_operacoes": 0,
                "ticket_medio": 0.0,
                "total_investido": 0.0,
                "produto_mais_frequente": None,
            }

        df = pd.DataFrame(transacoes)

        compras = df[df["tipo"] == "Compra"]

        total_investido = float(compras["valor_total"].sum())
        ticket_medio = (
            float(compras["valor_total"].mean()) if not compras.empty else 0.0
        )

        produto_mais_frequente = (
            df["produto"].mode().iloc[0] if not df["produto"].empty else None
        )

        return {
            "quantidade_operacoes": int(len(df)),
            "ticket_medio": round(ticket_medio, 2),
            "total_investido": round(total_investido, 2),
            "produto_mais_frequente": produto_mais_frequente,
        }