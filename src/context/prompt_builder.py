from pathlib import Path
class PromptBuilder:
    """
    Responsável por montar o prompt completo enviado ao LLM.
    """

    def __init__(self, prompts_path: str = "prompts"):

        self.prompts = Path(prompts_path)


    def _read(self, filename: str) -> str:

        file = self.prompts / filename

        with open(file, encoding="utf-8") as f:
            return f.read()


    def build_prompt(
        self,
        context: dict,
        question: str,
    ) -> str:

        system_prompt = self._read("system_prompt.md")

        guardrails = self._read("guardrails.md")

        few_shots = self._read("few_shots.md")

        output_format = self._read("output_format.md")

        context_template = self._read("context_template.md")

        context_text = context_template.format(
            perfil=context["perfil"],
            carteira=context["carteira"],
            transacoes=context["transacoes"],
            historico=context["historico"],
            produtos=context["produtos"],
            knowledge="",
            user_question=question,
        )

        prompt = f"""

{system_prompt}

{guardrails}

{few_shots}

{context_text}

{output_format}
"""

        return prompt.strip()