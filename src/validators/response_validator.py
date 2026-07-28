import re
class ResponseValidator:
    """
    Analisa a resposta gerada pelo modelo de linguagem e sinaliza
    problemas de estrutura, fundamentação ou linguagem de certeza
    absoluta, evitando que o usuário receba respostas não confiáveis.
    """
    EXPECTED_SECTIONS = [
        "Resumo",
        "Análise",
        "Fundamentação",
        "Riscos",
        "Conclusão",
    ]
    FORBIDDEN_EXPRESSIONS = [
        r"com\s+certeza\s+absoluta",
        r"garantid[oa]s?\s+de\s+lucro",
        r"n(ã|a)o\s+h(á|a)\s+risco",
        r"investimento\s+seguro\s+100%",
        r"vai\s+subir\s+com\s+certeza",
        r"vai\s+cair\s+com\s+certeza",
        r"retorno\s+garantido",
    ]

    def validate(self, response: str) -> dict:
        """
        Executa as validações e retorna um relatório estruturado com
        o resultado de cada verificação.
        """

        if not response or not response.strip():
            return {
                "valido": False,
                "erros": ["A resposta gerada está vazia."],
                "secoes_ausentes": self.EXPECTED_SECTIONS,
                "expressoes_proibidas_encontradas": [],
            }

        erros = []

        secoes_ausentes = self._check_sections(response)
        if secoes_ausentes:
            erros.append(
                "A resposta não segue integralmente a estrutura definida "
                "em output_format.md."
            )

        expressoes_encontradas = self._check_forbidden_expressions(response)
        if expressoes_encontradas:
            erros.append(
                "A resposta contém afirmações de certeza absoluta, "
                "violando as regras de anti-alucinação."
            )

        return {
            "valido": len(erros) == 0,
            "erros": erros,
            "secoes_ausentes": secoes_ausentes,
            "expressoes_proibidas_encontradas": expressoes_encontradas,
        }

    def _check_sections(self, response: str) -> list[str]:
        """
        Verifica quais seções esperadas não foram encontradas na
        resposta.
        """

        return [
            secao
            for secao in self.EXPECTED_SECTIONS
            if secao.lower() not in response.lower()
        ]

    def _check_forbidden_expressions(self, response: str) -> list[str]:
        """
        Verifica se a resposta contém expressões que caracterizam
        previsões com certeza absoluta ou promessas de rentabilidade.
        """

        lowered = response.lower()

        return [
            padrao
            for padrao in self.FORBIDDEN_EXPRESSIONS
            if re.search(padrao, lowered)
        ]