from pathlib import Path
import json
import pandas as pd

class ContextBuilder:
    """
    Responsável por recuperar e organizar todos os dados necessários para
    construir o contexto enviado ao modelo de linguagem.
    """

    def __init__(self, data_path: str = "data"):
        self.data_path = Path(data_path)

    def load_profile(self, cliente_id: int) -> dict:

        file = self.data_path / "perfil_investidor.json"

        with open(file, encoding="utf-8") as f:
            perfis = json.load(f)

        for perfil in perfis:
            if perfil["cliente_id"] == cliente_id:
                return perfil

        return {}

    def load_portfolio(self, cliente_id: int):

        file = self.data_path / "carteira.csv"

        carteira = pd.read_csv(file)

        return carteira[carteira["cliente_id"] == cliente_id].to_dict(
            orient="records"
        )

    def load_transactions(self, cliente_id: int):

        file = self.data_path / "transacoes.csv"

        transacoes = pd.read_csv(file)

        return transacoes[
            transacoes["cliente_id"] == cliente_id
        ].to_dict(orient="records")

    def load_products(self):

        file = self.data_path / "produtos_financeiros.json"

        with open(file, encoding="utf-8") as f:
            return json.load(f)

    def load_history(self, cliente_id: int):

        file = self.data_path / "historico_atendimento.csv"

        if not file.exists():
            return []

        historico = pd.read_csv(file)

        return historico[
            historico["cliente_id"] == cliente_id
        ].to_dict(orient="records")

    def build_context(self, cliente_id: int) -> dict:

        return {
            "perfil": self.load_profile(cliente_id),
            "carteira": self.load_portfolio(cliente_id),
            "transacoes": self.load_transactions(cliente_id),
            "historico": self.load_history(cliente_id),
            "produtos": self.load_products(),
        }