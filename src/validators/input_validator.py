import re
from src.config import MAX_QUESTION_LENGTH, MIN_QUESTION_LENGTH

class InputValidationError(Exception):
    """
    Exceção levantada quando a pergunta do usuário não passa nas
    validações de entrada.
    """


class InputValidator:
    """
    Realiza a validação e sanitização das perguntas recebidas do
    usuário antes de seguirem para a construção do contexto e do
    prompt.
    """
    BLOCKED_PATTERNS = [
        r"dados\s+(financeiros\s+)?de\s+outro\s+cliente",
        r"informa(ç|c)ões?\s+(financeiras\s+)?de\s+outro\s+cliente",
        r"ignore\s+as\s+instru(ç|c)ões",
        r"esque(ç|c)a\s+suas\s+regras",
        r"voc(ê|e)\s+n(ã|a)o\s+(é|e)\s+um\s+agente",
    ]

    def validate(self, question: str) -> str:
        """
        Valida e retorna a pergunta sanitizada.

        Levanta InputValidationError caso a pergunta seja inválida.
        """

        if question is None:
            raise InputValidationError("A pergunta não pode ser vazia.")

        clean_question = question.strip()

        if len(clean_question) < MIN_QUESTION_LENGTH:
            raise InputValidationError(
                "A pergunta é muito curta para ser processada."
            )

        if len(clean_question) > MAX_QUESTION_LENGTH:
            raise InputValidationError(
                f"A pergunta excede o limite de {MAX_QUESTION_LENGTH} "
                "caracteres."
            )

        self._check_blocked_patterns(clean_question)

        return clean_question

    def _check_blocked_patterns(self, question: str) -> None:
        """
        Verifica se a pergunta tenta acessar dados de terceiros ou
        manipular as instruções do agente.
        """

        lowered = question.lower()

        for pattern in self.BLOCKED_PATTERNS:
            if re.search(pattern, lowered):
                raise InputValidationError(
                    "Não é possível processar essa solicitação, pois "
                    "ela envolve acesso a dados de terceiros ou tenta "
                    "alterar o comportamento do agente."
                )

    def is_valid(self, question: str) -> bool:
        """
        Retorna True/False sem levantar exceção, útil para validações
        rápidas em interfaces (ex.: chat).
        """

        try:
            self.validate(question)
            return True
        except InputValidationError:
            return False