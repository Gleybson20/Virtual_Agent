class MacroService:
    """
    Fornece contexto conceitual sobre indicadores macroeconômicos e
    sua relação com classes de ativos.
    """

    INDICADORES = {
        "selic": {
            "nome": "Taxa Selic",
            "descricao": (
                "Taxa básica de juros da economia brasileira, definida "
                "pelo Comitê de Política Monetária (Copom)."
            ),
            "impactos": {
                "renda_fixa": (
                    "Selic mais alta tende a elevar a rentabilidade de "
                    "produtos pós-fixados (Tesouro Selic, CDB, LCI/LCA)."
                ),
                "renda_variavel": (
                    "Selic mais alta eleva o custo de capital das "
                    "empresas e tende a pressionar o valuation de ações, "
                    "tornando a renda fixa relativamente mais atrativa."
                ),
                "fundos_imobiliarios": (
                    "Selic mais alta tende a pressionar o preço de FIIs, "
                    "já que o custo de oportunidade em relação à renda "
                    "fixa aumenta."
                ),
                "credito": "Selic mais alta encarece o crédito na economia.",
            },
        },
        "ipca": {
            "nome": "IPCA (Inflação)",
            "descricao": (
                "Índice oficial de inflação do Brasil, utilizado como "
                "referência para a meta de inflação e para títulos "
                "indexados como o Tesouro IPCA+."
            ),
            "impactos": {
                "renda_fixa": (
                    "Títulos indexados ao IPCA protegem o poder de "
                    "compra do investidor no longo prazo."
                ),
                "renda_variavel": (
                    "Inflação elevada tende a pressionar custos "
                    "corporativos e pode reduzir margens, dependendo do "
                    "poder de repasse de preços de cada setor."
                ),
                "poder_de_compra": (
                    "Inflação elevada reduz o poder de compra do "
                    "capital não investido ou investido em produtos sem "
                    "proteção inflacionária."
                ),
            },
        },
        "cambio": {
            "nome": "Taxa de Câmbio (USD/BRL)",
            "descricao": (
                "Preço relativo entre o real e outras moedas, "
                "influenciado por fluxo de capital, juros e cenário "
                "externo."
            ),
            "impactos": {
                "renda_variavel": (
                    "Empresas exportadoras tendem a se beneficiar da "
                    "desvalorização do real, enquanto importadoras "
                    "tendem a ser prejudicadas."
                ),
                "investimentos_internacionais": (
                    "A variação cambial afeta diretamente a "
                    "rentabilidade de ativos internacionais, como ETFs "
                    "e BDRs, quando convertidos para reais."
                ),
            },
        },
        "pib": {
            "nome": "PIB (Produto Interno Bruto)",
            "descricao": (
                "Mede o valor total de bens e serviços produzidos na "
                "economia em um determinado período, sendo um dos "
                "principais indicadores de atividade econômica."
            ),
            "impactos": {
                "renda_variavel": (
                    "Crescimento do PIB tende a favorecer setores "
                    "cíclicos e o desempenho de empresas ligadas ao "
                    "consumo interno."
                ),
                "emprego_e_renda": (
                    "Crescimento do PIB costuma estar associado a "
                    "geração de emprego e renda, impactando o consumo "
                    "e a poupança das famílias."
                ),
            },
        },
    }

    def get_indicator(self, chave: str) -> dict:
        """
        Retorna as informações conceituais de um indicador
        macroeconômico específico.
        """

        return self.INDICADORES.get(chave.strip().lower(), {})

    def list_indicators(self) -> list[str]:
        """
        Lista as chaves dos indicadores disponíveis na base de
        conhecimento macroeconômico.
        """

        return list(self.INDICADORES.keys())

    def explain_impact(self, chave: str, classe_ativo: str) -> str:
        """
        Retorna a explicação do impacto de um indicador sobre uma
        classe de ativo específica.

        Caso não haja fundamentação disponível, retorna uma string
        vazia, permitindo que o agente informe a limitação em vez de
        inventar uma explicação.
        """

        indicador = self.get_indicator(chave)

        if not indicador:
            return ""

        return indicador.get("impactos", {}).get(classe_ativo.strip().lower(), "")

    def build_knowledge_snippet(self, chave: str) -> str:
        """
        Monta um trecho textual com o conhecimento macroeconômico
        consolidado, pronto para ser incorporado ao contexto enviado
        ao LLM (campo "Conhecimento Recuperado" do context_template).
        """

        indicador = self.get_indicator(chave)

        if not indicador:
            return ""

        linhas = [f"{indicador['nome']}: {indicador['descricao']}"]

        for classe, impacto in indicador.get("impactos", {}).items():
            linhas.append(f"- Impacto em {classe.replace('_', ' ')}: {impacto}")

        return "\n".join(linhas)