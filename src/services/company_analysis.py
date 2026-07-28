class CompanyAnalysisService:

    INDICADORES_PADRAO = [
        "roe",
        "roa",
        "margem_liquida",
        "p_l",
        "p_vp",
        "dividend_yield",
        "divida_liquida_ebitda",
        "crescimento_lucros",
    ]

    DESCRICAO_INDICADORES = {
        "roe": "Retorno sobre o Patrimônio Líquido — mede a eficiência "
        "da empresa em gerar lucro a partir do capital próprio.",
        "roa": "Retorno sobre os Ativos — mede a eficiência da empresa "
        "em gerar lucro a partir do total de ativos.",
        "margem_liquida": "Percentual da receita que se converte em "
        "lucro líquido.",
        "p_l": "Preço sobre Lucro — indica quantos anos de lucro "
        "seriam necessários para pagar o preço atual da ação.",
        "p_vp": "Preço sobre Valor Patrimonial — compara o preço de "
        "mercado ao patrimônio líquido por ação.",
        "dividend_yield": "Percentual de proventos distribuídos em "
        "relação ao preço da ação.",
        "divida_liquida_ebitda": "Mede o nível de endividamento da "
        "empresa em relação à sua geração de caixa operacional.",
        "crescimento_lucros": "Variação percentual do lucro em um "
        "determinado período.",
    }

    def validate_indicators(self, empresa: dict) -> list[str]:
        """
        Verifica quais indicadores padrão estão ausentes nos dados
        informados sobre uma empresa.

        Isso permite que o agente informe explicitamente quando não
        houver dados suficientes para uma comparação completa, em vez
        de presumir ou inventar valores.
        """

        return [
            indicador
            for indicador in self.INDICADORES_PADRAO
            if indicador not in empresa or empresa[indicador] in (None, "")
        ]

    def compare(self, empresa_a: dict, empresa_b: dict) -> dict:
        """
        Estrutura a comparação entre duas empresas a partir dos
        indicadores fornecidos.

        Retorna um dicionário organizado por indicador, além da lista
        de indicadores ausentes em cada empresa, para que o agente
        seja transparente sobre eventuais limitações de dados.
        """

        comparacao = {}

        for indicador in self.INDICADORES_PADRAO:
            comparacao[indicador] = {
                "descricao": self.DESCRICAO_INDICADORES[indicador],
                empresa_a.get("nome", "Empresa A"): empresa_a.get(indicador),
                empresa_b.get("nome", "Empresa B"): empresa_b.get(indicador),
            }

        return {
            "comparacao": comparacao,
            "indicadores_ausentes_empresa_a": self.validate_indicators(empresa_a),
            "indicadores_ausentes_empresa_b": self.validate_indicators(empresa_b),
        }

    def build_knowledge_snippet(self, empresa_a: dict, empresa_b: dict) -> str:
        """
        Monta um trecho textual pronto para ser incorporado ao
        contexto enviado ao LLM, resumindo os indicadores disponíveis
        e os ausentes para a comparação solicitada.
        """

        resultado = self.compare(empresa_a, empresa_b)

        linhas = [
            f"Comparação entre {empresa_a.get('nome', 'Empresa A')} e "
            f"{empresa_b.get('nome', 'Empresa B')}:"
        ]

        for indicador, valores in resultado["comparacao"].items():
            nome_a = empresa_a.get("nome", "Empresa A")
            nome_b = empresa_b.get("nome", "Empresa B")
            linhas.append(
                f"- {indicador.upper()}: {nome_a}="
                f"{valores.get(nome_a, 'N/D')} | {nome_b}="
                f"{valores.get(nome_b, 'N/D')}"
            )

        if resultado["indicadores_ausentes_empresa_a"]:
            linhas.append(
                f"Indicadores ausentes para {empresa_a.get('nome', 'Empresa A')}: "
                + ", ".join(resultado["indicadores_ausentes_empresa_a"])
            )

        if resultado["indicadores_ausentes_empresa_b"]:
            linhas.append(
                f"Indicadores ausentes para {empresa_b.get('nome', 'Empresa B')}: "
                + ", ".join(resultado["indicadores_ausentes_empresa_b"])
            )

        return "\n".join(linhas)