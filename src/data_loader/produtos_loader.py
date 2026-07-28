from pathlib import Path
import json
from src.config import DATA_DIR

class ProdutosLoader:
    """
    Carrega e consulta o catálogo de produtos financeiros disponível
    para os clientes.
    """

    def __init__(self, data_path: Path = DATA_DIR):
        self.file = Path(data_path) / "produtos_financeiros.json"

    def load_all(self) -> list[dict]:
        """
        Retorna o catálogo completo de produtos financeiros.
        """

        if not self.file.exists():
            return []

        with open(self.file, encoding="utf-8") as f:
            return json.load(f)

    def get_by_id(self, produto_id: int) -> dict:
        """
        Retorna um produto específico pelo identificador.
        """

        for produto in self.load_all():
            if produto.get("produto_id") == produto_id:
                return produto

        return {}

    def get_by_category(self, categoria: str) -> list[dict]:
        """
        Retorna todos os produtos de uma determinada categoria
        (ex.: "Renda Fixa", "ETF", "FII").
        """

        categoria = categoria.strip().lower()

        return [
            produto
            for produto in self.load_all()
            if produto.get("categoria", "").strip().lower() == categoria
        ]

    def get_recommended_for_profile(self, perfil: str) -> list[dict]:
        """
        Retorna os produtos compatíveis com um determinado perfil de
        risco (ex.: "Conservador", "Moderado", "Arrojado").

        Essa consulta é utilizada pelos serviços de recomendação para
        garantir que nenhuma sugestão seja incompatível com o perfil
        do investidor.
        """

        perfil = perfil.strip().lower()

        return [
            produto
            for produto in self.load_all()
            if perfil
            in [p.strip().lower() for p in produto.get("perfil_recomendado", [])]
        ]