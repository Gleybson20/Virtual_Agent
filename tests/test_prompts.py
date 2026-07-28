from src.context.context_builder import ContextBuilder
from src.context.prompt_builder import PromptBuilder

CLIENTE_EXISTENTE = 1


def _build_sample_prompt() -> str:
    context_builder = ContextBuilder()
    prompt_builder = PromptBuilder()

    contexto = context_builder.build_context(CLIENTE_EXISTENTE)

    return prompt_builder.build_prompt(
        contexto, "Tenho R$ 20.000 para investir. Qual a melhor estratégia?"
    )


def test_prompt_contem_system_prompt():
    prompt = _build_sample_prompt()
    assert "Advisor Invest" in prompt


def test_prompt_contem_guardrails():
    prompt = _build_sample_prompt()
    assert "Guardrails" in prompt


def test_prompt_contem_few_shots():
    prompt = _build_sample_prompt()
    assert "Few Shots" in prompt


def test_prompt_contem_pergunta_do_usuario():
    prompt = _build_sample_prompt()
    assert "Tenho R$ 20.000 para investir" in prompt


def test_prompt_contem_perfil_do_cliente():
    prompt = _build_sample_prompt()
    assert "Carlos Eduardo Silva" in prompt


def test_prompt_segue_ordem_definida():
    """
    Verifica se as seções aparecem na ordem definida em
    prompts/prompt_builder.md: System Prompt -> Guardrails ->
    Few Shots -> Contexto -> Pergunta -> Formato de Resposta.
    """

    prompt = _build_sample_prompt()

    posicao_system = prompt.find("Advisor Invest")
    posicao_guardrails = prompt.find("Guardrails")
    posicao_few_shots = prompt.find("Few Shots")
    posicao_contexto = prompt.find("Context Template")
    posicao_output = prompt.find("Output Format")

    assert posicao_system < posicao_guardrails < posicao_few_shots
    assert posicao_few_shots < posicao_contexto < posicao_output