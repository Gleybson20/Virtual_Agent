from pathlib import Path
import json

from src.config import DATA_DIR


class PerfilLoader:
    """
    Carrega e consulta o cadastro de investidores.
    """

    def __init__(self, data_path: Path = DATA_DIR):
        self.file = Path(data_path) / "perfil_investidor.json"

    def load_all(self) -> list[dict]:
        """
        Retorna o cadastro completo de investidores.
        """

        if not self.file.exists():
            return []

        with open(self.file, encoding="utf-8") as f:
            return json.load(f)

    def get_by_id(self, cliente_id: int) -> dict:
        """
        Retorna o perfil de um investidor específico.

        Caso o cliente não seja encontrado, retorna um dicionário vazio,
        permitindo que o agente informe ausência de dados em vez de
        presumir um perfil inexistente.
        """

        for perfil in self.load_all():
            if perfil.get("cliente_id") == cliente_id:
                return perfil

        return {}

    def exists(self, cliente_id: int) -> bool:
        """
        Verifica se o cliente possui cadastro na base de conhecimento.
        """

        return bool(self.get_by_id(cliente_id))