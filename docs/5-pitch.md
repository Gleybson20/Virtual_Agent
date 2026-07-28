# Pitch (3 minutos)

> [!TIP]
> Este roteiro foi elaborado para uma apresentação de aproximadamente 3 minutos, destacando o problema, a solução proposta, a arquitetura do agente e seus diferenciais.

---

# Roteiro Sugerido

## 1. O Problema (30 segundos)

Tomar decisões de investimento exige interpretar uma grande quantidade de informações financeiras, econômicas e corporativas. Muitos investidores possuem dificuldade em entender conceitos financeiros, analisar indicadores macroeconômicos ou comparar empresas de forma fundamentada.

Além disso, assistentes tradicionais costumam responder apenas perguntas isoladas, sem considerar o perfil do investidor, seu histórico de movimentações ou seu contexto financeiro, gerando respostas genéricas e pouco personalizadas.

O problema que buscamos resolver é justamente transformar essas informações dispersas em análises claras, fundamentadas e adaptadas ao contexto de cada investidor.

---

## 2. A Solução (1 minuto)

Para resolver esse problema desenvolvemos o **Advisor Invest**, um Agente Financeiro Inteligente baseado em IA Generativa.

O Advisor Invest foi projetado para atuar como um consultor virtual especializado em investimentos, combinando conhecimentos de finanças corporativas, economia, análise fundamentalista e gestão de investimentos.

Antes de responder qualquer pergunta, o agente utiliza uma Base de Conhecimento composta por quatro conjuntos de dados:

- Perfil do Investidor
- Histórico de Transações
- Histórico de Atendimento
- Produtos Financeiros

Essas informações são organizadas por um processo de **Context Engineering**, que constrói um contexto personalizado e o envia juntamente com a pergunta ao modelo de linguagem.

Dessa forma, o agente consegue:

- Explicar conceitos financeiros.
- Interpretar indicadores macroeconômicos.
- Comparar empresas e setores.
- Fundamentar todas as análises.
- Adaptar as respostas ao perfil do investidor.
- Evitar recomendações incompatíveis com os objetivos do usuário.

Além disso, o projeto foi desenvolvido com estratégias para reduzir alucinações, deixando explícito quando não houver informações suficientes para responder uma pergunta.

---

## 3. Demonstração (1 minuto)

Durante a demonstração serão apresentados:

### Slide 1

Arquitetura geral do projeto.

Mostrar a organização do repositório e os principais componentes:

- Base de Conhecimento
- Prompts
- Context Builder
- LLM
- Camada de Validação

---

### Slide 2

Fluxo de funcionamento.

Demonstrar o seguinte processo:

Usuário → Construção do Contexto → Modelo de Linguagem → Resposta Fundamentada.

---

### Slide 3

Exemplo de interação.

Pergunta:

> "Tenho perfil moderado. Vale investir em ações?"

Mostrar que o agente:

- consulta o Perfil do Investidor;
- utiliza o Histórico de Transações;
- considera os Produtos Financeiros disponíveis;
- responde de forma personalizada;
- explica os riscos;
- fundamenta a conclusão utilizando conceitos financeiros.

---

### Slide 4

Documentação produzida.

Apresentar rapidamente:

- Documentação do Agente
- Base de Conhecimento
- Engenharia de Prompts
- Métricas de Avaliação

Demonstrando que toda a solução foi planejada para ser escalável e pronta para futura implementação.

---

## 4. Diferencial e Impacto (30 segundos)

O principal diferencial do Advisor Invest está na forma como utiliza contexto para produzir respostas.

Em vez de responder apenas à pergunta do usuário, o agente considera informações sobre seu perfil, histórico financeiro e produtos disponíveis, entregando análises muito mais relevantes e personalizadas.

Outro diferencial importante é o foco em transparência e segurança. O agente evita inventar informações, diferencia fatos de hipóteses e fundamenta todas as suas conclusões em conceitos reconhecidos do mercado financeiro.

Como impacto, essa solução pode contribuir para ampliar a educação financeira, apoiar investidores em suas decisões e tornar o acesso à informação financeira mais claro, confiável e acessível.

---

# Checklist do Pitch

- [x] Duração máxima de 3 minutos
- [x] Problema claramente definido
- [x] Solução apresentada
- [x] Fluxo de funcionamento explicado
- [x] Diferenciais destacados
- [ ] Demonstração prática (após implementação)
- [ ] Áudio e vídeo com boa qualidade

---