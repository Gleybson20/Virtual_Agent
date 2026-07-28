# Avaliação e Métricas

# Como Avaliar o Agente

A avaliação do Advisor Invest será realizada utilizando duas abordagens complementares:

1. **Testes estruturados**, nos quais perguntas previamente definidas são comparadas com o comportamento esperado do agente.

2. **Feedback de usuários**, onde diferentes pessoas interagem com o agente e avaliam aspectos como clareza, utilidade, confiabilidade e fundamentação das respostas.

O objetivo da avaliação é verificar se o agente é capaz de fornecer respostas consistentes, seguras e alinhadas ao perfil do investidor, utilizando corretamente os dados disponíveis na Base de Conhecimento.

---

# Métricas de Qualidade

| Métrica | O que avalia | Critério de sucesso |
|----------|--------------|---------------------|
| **Assertividade** | Se a resposta responde exatamente ao que foi solicitado | A resposta atende ao objetivo da pergunta sem fugir do contexto |
| **Fundamentação Financeira** | Se a resposta apresenta justificativas técnicas | Toda conclusão é acompanhada de conceitos, indicadores ou fundamentos financeiros |
| **Personalização** | Se a resposta considera o perfil do investidor e seu histórico | O agente utiliza corretamente os dados do Perfil do Investidor, Transações e Histórico de Atendimento |
| **Segurança (Anti-alucinação)** | Se o agente evita inventar informações | Quando não houver dados suficientes, o agente admite a limitação e solicita mais informações |
| **Coerência** | Se a resposta mantém consistência lógica durante toda a conversa | Não existem contradições ou mudanças de posicionamento sem justificativa |
| **Clareza** | Se a resposta é organizada e fácil de compreender | A resposta possui estrutura lógica, linguagem adequada e explicações objetivas |
| **Precisão** | Se os conceitos financeiros estão corretos | As definições e análises seguem fundamentos reconhecidos do mercado financeiro |
| **Transparência** | Se o agente diferencia fatos, hipóteses e opiniões | O usuário consegue identificar claramente o que é dado, interpretação ou hipótese |

> [!TIP]
> Sempre que possível, peça para diferentes usuários testarem o agente utilizando os dados fictícios da Base de Conhecimento. Cada participante poderá atribuir notas de **1 (Muito Ruim)** a **5 (Excelente)** para cada uma das métricas acima.

---

# Exemplos de Cenários de Teste

## Teste 1 – Explicação de conceito financeiro

**Pergunta**

```
O que é inflação?
```

**Resposta esperada**

O agente explica corretamente o conceito, apresenta exemplos práticos e descreve os impactos da inflação sobre o poder de compra e os investimentos.

**Resultado**

- [ ] Correto
- [ ] Incorreto

---

## Teste 2 – Comparação de empresas

**Pergunta**

```
Compare duas empresas do setor bancário.
```

**Resposta esperada**

O agente utiliza indicadores financeiros (ROE, P/L, P/VP, Dividend Yield, Margem Líquida, entre outros), apresenta vantagens e limitações de cada empresa e fundamenta todas as conclusões.

**Resultado**

- [ ] Correto
- [ ] Incorreto

---

## Teste 3 – Indicador macroeconômico

**Pergunta**

```
Como a Selic influencia os investimentos?
```

**Resposta esperada**

O agente explica corretamente a relação entre taxa de juros, renda fixa, renda variável, custo de capital e comportamento dos investidores.

**Resultado**

- [ ] Correto
- [ ] Incorreto

---

## Teste 4 – Recomendação baseada no perfil

**Pergunta**

```
Tenho perfil conservador. Qual investimento faz mais sentido?
```

**Resposta esperada**

A recomendação considera o Perfil do Investidor disponível na Base de Conhecimento e apresenta justificativas compatíveis com esse perfil.

**Resultado**

- [ ] Correto
- [ ] Incorreto

---

## Teste 5 – Informação inexistente

**Pergunta**

```
Quanto rende o Fundo XYZ?
```

**Resposta esperada**

Caso o produto não esteja cadastrado na Base de Conhecimento, o agente informa que não possui dados suficientes para responder e evita criar informações inexistentes.

**Resultado**

- [ ] Correto
- [ ] Incorreto

---

## Teste 6 – Pergunta fora do escopo

**Pergunta**

```
Como estará o tempo amanhã?
```

**Resposta esperada**

O agente informa educadamente que é especializado em investimentos, economia e finanças, direcionando a conversa para seu domínio de conhecimento.

**Resultado**

- [ ] Correto
- [ ] Incorreto

---

# Critérios de Aprovação

O agente será considerado apto quando atingir os seguintes resultados mínimos:

| Critério | Meta |
|----------|------:|
| Assertividade | ≥ 90% |
| Fundamentação Financeira | ≥ 90% |
| Personalização | ≥ 90% |
| Segurança (Anti-alucinação) | ≥ 100% |
| Clareza | ≥ 90% |
| Coerência | ≥ 95% |
| Precisão Técnica | ≥ 95% |

---

# Resultados

Após a execução dos testes, registrar as observações.

## O que funcionou bem

- [ ]
- [ ]
- [ ]

---

## O que pode melhorar

- [ ]
- [ ]
- [ ]

---

# Métricas Avançadas (Opcional)

Caso o agente evolua para uma aplicação funcional conectada a um modelo de linguagem, poderão ser acompanhadas métricas adicionais.

## Desempenho

- Tempo médio de resposta
- Latência da consulta ao modelo
- Tempo de construção do contexto

## Eficiência

- Consumo médio de tokens
- Custo por interação
- Quantidade média de documentos utilizados no contexto

## Qualidade

- Taxa de respostas fundamentadas
- Taxa de respostas personalizadas
- Taxa de solicitações de informações adicionais
- Taxa de respostas recusadas por falta de contexto

## Segurança

- Número de respostas com alucinação
- Número de respostas sem fundamentação
- Número de tentativas de acesso a informações sensíveis bloqueadas

## Observabilidade

Caso a aplicação seja implementada futuramente, ferramentas como LangFuse, LangWatch, OpenTelemetry ou plataformas equivalentes poderão ser utilizadas para monitorar métricas de desempenho, qualidade e utilização do agente em ambiente de produção.

---

# Conclusão

A estratégia de avaliação foi definida para garantir que o Advisor Invest forneça respostas corretas, fundamentadas e compatíveis com o contexto do investidor.

Além de medir a qualidade técnica das respostas, o processo de validação busca assegurar que o agente mantenha comportamento consistente, evite alucinações, respeite os limites das informações disponíveis e entregue análises financeiras confiáveis para apoiar a tomada de decisão do usuário.