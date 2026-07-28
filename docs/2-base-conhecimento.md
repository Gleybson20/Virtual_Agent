# Base de Conhecimento do Agente

## Objetivo

A Base de Conhecimento é responsável por fornecer ao Agente Financeiro todas as informações necessárias para gerar respostas contextualizadas, fundamentadas e personalizadas.

Os dados não são utilizados como treinamento do modelo de linguagem, mas sim como contexto dinâmico inserido durante cada interação. Dessa forma, o agente consegue compreender o perfil do usuário, seu histórico financeiro, seus investimentos e os produtos disponíveis antes de elaborar qualquer resposta.

---

# Arquitetura da Base de Conhecimento

A base de conhecimento é composta por quatro conjuntos principais de dados:

```
Perfil do Investidor
        │
        │
Histórico de Transações
        │
        │
Histórico de Atendimento
        │
        │
Produtos Financeiros
        │
        ▼
Context Builder
        │
        ▼
Prompt Context
        │
        ▼
LLM
        │
        ▼
Resposta Personalizada
```

Cada conjunto possui uma responsabilidade específica dentro do processo de construção do contexto enviado ao modelo.

---

# Fontes de Dados

## 1. Perfil do Investidor

**Arquivo**

```
data/perfil_investidor.json
```

### Objetivo

Identificar quem é o cliente e quais são suas características como investidor.

### Principais informações

- ID do cliente
- Nome
- Idade
- Perfil de risco
- Objetivo financeiro
- Horizonte de investimento
- Patrimônio
- Renda mensal
- Tolerância ao risco
- Necessidade de liquidez

### Utilização pelo agente

Essas informações permitem que o agente adapte todas as respostas ao perfil do investidor.

Exemplos:

- Adequação de produtos financeiros.
- Explicação do nível de risco.
- Personalização das recomendações.
- Avaliação de compatibilidade entre investimentos e objetivos.

---

## 2. Histórico de Transações

**Arquivo**

```
data/transacoes.csv
```

### Objetivo

Registrar o comportamento financeiro do cliente ao longo do tempo.

### Principais informações

- Data
- Tipo da operação
- Produto
- Categoria
- Valor
- Quantidade
- Situação

### Utilização pelo agente

Permite identificar:

- frequência de investimentos;
- ticket médio;
- patrimônio investido;
- produtos mais utilizados;
- comportamento de compra e venda;
- evolução da carteira.

Essas informações ajudam o agente a compreender os hábitos do investidor antes de responder qualquer pergunta.

---

## 3. Produtos Financeiros

**Arquivo**

```
data/produtos_financeiros.json
```

### Objetivo

Representar o catálogo de investimentos disponível para o cliente.

### Principais informações

- Nome do produto
- Categoria
- Rentabilidade
- Risco
- Liquidez
- Tributação
- Valor mínimo
- Descrição
- Público recomendado

### Utilização pelo agente

O agente utiliza este conjunto para:

- explicar produtos financeiros;
- comparar alternativas;
- sugerir investimentos compatíveis com o perfil do cliente;
- justificar vantagens e riscos de cada opção.

---

## 4. Histórico de Atendimento

**Arquivo**

```
data/historico_atendimento.csv
```

### Objetivo

Armazenar o histórico de relacionamento entre o cliente e o agente.

### Principais informações

- Data
- Assunto
- Pergunta
- Resposta
- Observações
- Pendências

### Utilização pelo agente

Permite:

- manter continuidade das conversas;
- evitar repetir perguntas;
- compreender dúvidas recorrentes;
- considerar decisões anteriores durante novas análises.

---

# Relacionamento entre os Dados

```
                    Cliente
                       │
      ┌────────────────┼───────────────┐
      │                │               │
      ▼                ▼               ▼

Perfil        Transações       Histórico

      └────────────────┼───────────────┘
                       │
                       ▼

             Produtos Financeiros

                       │
                       ▼

          Contexto enviado ao LLM
```

Todos os dados possuem como chave principal o identificador do cliente (cliente_id), permitindo consolidar as informações em um único contexto antes da interação com o modelo.

---

# Estratégia de Integração com o LLM

Sempre que uma pergunta é enviada pelo usuário, o sistema executa o seguinte fluxo:

```
Usuário faz uma pergunta

        │

        ▼

Identificar o cliente

        │

        ▼

Consultar Perfil

        │

        ▼

Consultar Histórico de Transações

        │

        ▼

Consultar Histórico de Atendimento

        │

        ▼

Consultar Produtos Financeiros

        │

        ▼

Construir o Contexto

        │

        ▼

Enviar Contexto + Pergunta para o LLM

        │

        ▼

Gerar Resposta
```

Essa abordagem garante que o modelo responda considerando o contexto completo do cliente e não apenas a pergunta isolada.

---

# Estrutura do Contexto Enviado ao Prompt

Antes da geração da resposta, as informações recuperadas são organizadas em um contexto estruturado.

Exemplo simplificado:

```text
Perfil do Investidor

Nome: João Silva

Perfil: Moderado

Objetivo: Aposentadoria

Horizonte: Longo Prazo

Patrimônio: R$ 250.000

--------------------------------------------------

Últimas Transações

• Compra Tesouro IPCA

• Compra ETF IVVB11

• Compra CDB

--------------------------------------------------

Últimos Atendimentos

• Demonstrou receio sobre renda variável

• Solicitou investimentos de longo prazo

--------------------------------------------------

Produtos Disponíveis

Tesouro Selic

Tesouro IPCA

CDB

LCI

ETF

Fundos Multimercado

--------------------------------------------------

Pergunta

"Tenho R$ 20.000 para investir. Qual a melhor estratégia?"
```

Esse contexto é anexado ao System Prompt do agente antes da chamada ao modelo de linguagem.

---

# Benefícios da Estratégia

A utilização dessa arquitetura permite:

- Personalização das respostas.
- Continuidade das conversas.
- Maior precisão das análises.
- Redução de alucinações.
- Recomendações compatíveis com o perfil do investidor.
- Justificativas baseadas em dados reais do cliente.

---

# Atualização da Base de Conhecimento

Os dados poderão ser atualizados de forma independente.

| Arquivo | Frequência de atualização |
|----------|--------------------------|
| perfil_investidor.json | Quando houver alteração cadastral |
| transacoes.csv | A cada nova movimentação |
| historico_atendimento.csv | Após cada atendimento |
| produtos_financeiros.json | Sempre que houver novos produtos ou alterações nas regras |

Essa separação facilita a manutenção da base de conhecimento e permite que o agente trabalhe sempre com informações atualizadas.