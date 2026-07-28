from pathlib import Path
import pandas as pd
from src.config import DATA_DIR

class AtendimentoLoader:
    """
    Carrega e consulta o histórico de relacionamento entre o cliente
    e o agente.
    """

    def __init__(self, data_path: Path = DATA_DIR):
        self.file = Path(data_path) / "historico_atendimento.csv"

    def load_all(self) -> pd.DataFrame:
        """
        Retorna todo o histórico de atendimento cadastrado.

        Caso o arquivo ainda não exista, retorna um DataFrame vazio
        em vez de gerar erro, já que o histórico é opcional para o
        funcionamento do agente.
        """

        if not self.file.exists():
            return pd.DataFrame()

        return pd.read_csv(self.file)

    def get_by_client(self, cliente_id: int) -> list[dict]:
        """
        Retorna os atendimentos anteriores de um cliente específico,
        ordenados do mais antigo para o mais recente.
        """

        df = self.load_all()

        if df.empty:
            return []

        cliente_df = df[df["cliente_id"] == cliente_id].sort_values("data")

        return cliente_df.to_dict(orient="records")

    def get_last_interactions(self, cliente_id: int, limit: int = 3) -> list[dict]:
        """
        Retorna as últimas interações do cliente, úteis para dar
        continuidade à conversa sem repetir perguntas já respondidas.
        """

        historico = self.get_by_client(cliente_id)

        return historico[-limit:]