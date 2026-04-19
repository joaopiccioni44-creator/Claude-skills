---
name: linkedin-360brew
description: >
  Cria, otimiza e revisa posts para o LinkedIn alinhados ao algoritmo 360Brew (2025-2026).
  Use esta skill sempre que o usuário pedir para criar, melhorar, revisar ou adaptar
  um post do LinkedIn — ou quiser estratégias de conteúdo, hooks, carrosseis,
  CTAs e pilares temáticos para a plataforma. Também use quando o usuário mencionar
  alcance, impressões, saves, thought leadership ou personal branding no LinkedIn.
---

# LinkedIn 360Brew — Skill de Conteúdo

## O que é o 360Brew

O **360Brew** é o foundation model de 150 bilhões de parâmetros que substituiu **todos** os sistemas de ranking do LinkedIn. Construído sobre a arquitetura Mixtral 8x22 (Mixture of Experts) e publicado no arXiv em janeiro de 2025, ele começou a impactar resultados visivelmente a partir do segundo semestre de 2024 e está em pleno deployment desde o início de 2026.

**A mudança filosófica central:** o sistema antigo media *o que você postava*; o novo mede *quem você é*.

O 360Brew não pergunta mais "quantos likes esse post teve nas primeiras horas?". Ele constrói um prompt em linguagem natural para cada potencial viewer e se pergunta: *"Dado quem essa pessoa é e o que ela engajou recentemente, esse post vai gerar valor real para ela?"*

---

## Os 5 Pilares do 360Brew

### 1. Alinhamento Perfil ↔ Conteúdo (Semantic Identity)

O 360Brew lê seu perfil e seus posts como **um documento semântico unificado**. Se seu headline diz "Especialista em Mercado Financeiro" mas você posta sobre produtividade geral, o algoritmo classifica o conteúdo como off-topic e limita a distribuição.

**Checklist de alinhamento:**
- Headline contém os 2-3 pilares temáticos do conteúdo
- Seção "Sobre" usa as mesmas palavras-chave dos posts
- Skills e experiências validam a expertise declarada nos posts
- Featured section conecta à proposta de valor dos conteúdos

### 2. Consistência Temática (Topic Authority)

O sistema constrói um "credibility cluster" em torno de quem você é. Isso leva **~90 dias de posting consistente** para se estabelecer. Topic hopping dilui autoridade em *todos* os temas simultaneamente.

**Regra 80/20:** 80% dos posts dentro dos 2-3 pilares definidos. 20% podem explorar temas adjacentes sem destruir o cluster.

### 3. Depth Score (Profundidade de Engajamento)

O 360Brew substituiu "likes" por uma métrica composta de **profundidade real**:

| Sinal | Peso Relativo |
|-------|--------------|
| Save | 5-10x mais que like |
| DM originado do post | Sinal mais forte |
| Comment com perspectiva própria | Alto |
| Dwell time (tempo na leitura) | Alto |
| "See More" click + leitura completa | Médio-alto |
| Like | Baixo |
| Comment genérico ("Ótimo post!") | Quase nulo ou negativo |

> ⚠️ **Clickbait penalty:** Se o usuário clica em "Ver mais" mas abandona em segundos, o sistema registra isso como sinal negativo (hook enganoso).

### 4. In-Context Learning (ICL)

O 360Brew aprende em tempo real sobre cada viewer. Cada comentário substantivo que alguém faz em um post sobre "mercado de crédito" sinaliza ao sistema que aquela pessoa deve ver mais conteúdo sobre crédito. Isso significa que **os comentários que você atrai treinam o algoritmo** sobre seu público-alvo.

### 5. Multi-Surface Distribution

O modelo opera simultaneamente em feed, busca, notificações, newsletters e "People You May Know". Conteúdo bem avaliado ganha distribuição across surfaces — e posts de alta qualidade podem ser reativados pelo algoritmo **4-7 dias após publicação** se atingirem novos thresholds de relevância.

---

## O que o 360Brew Recompensa vs. Penaliza

### ✅ Recompensa
- Expertise real e opiniões fundamentadas
- Estrutura lógica e argumentativa (o modelo é treinado em logical coherence)
- Conteúdo "save-worthy" — frameworks, dados, checklists que as pessoas vão querer rever
- Comentários substantivos em outros posts do seu nicho
- Voz única e autêntica (credibility scoring detecta escrita genérica de IA)
- Perguntas que provocam reflexão real ao fim do post

### ❌ Penaliza
- Engagement bait: "Comente FIRE para receber o guia" (-70% de alcance)
- Engagement pods: padrões de timing detectáveis (mesmas pessoas, janela de 8-10 min)
- Conteúdo genérico de IA sem personalidade
- Hashtag stuffing (hashtags não influenciam mais a distribuição semântica)
- Tagging massivo de pessoas sem contexto
- Links externos no corpo do post (penalização por off-platform behavior)
- Alta frequência com baixa qualidade (1-2 posts excelentes/semana > 7 posts mediocres)
- **Posts de newsletter como teaser + card** — o algoritmo lê como tráfego de saída e freia a distribuição (ver seção específica abaixo)

---

## Framework de Criação de Post

### Estrutura Base

```
[HOOK — 210 caracteres máximo antes do "Ver mais"]

[CORPO — desenvolvimento com estrutura lógica]

[ENCERRAMENTO — CTA reflexivo ou convite a perspectiva]
```

### O Hook (Primeiros 210 Caracteres)

O 360Brew aplica **3-5x mais atenção** ao início do post. O fenômeno "Lost in Distance" significa que o modelo prioriza semanticamente o que aparece primeiro.

**Tipos de hook eficazes:**

| Tipo | Exemplo | Melhor para |
|------|---------|-------------|
| **Tensão de Identidade** | "A alucinação dos C-levels." | Alcance máximo — nomeia grupo, cria pressão de identificação |
| **Distinção Analítica** | "Há uma diferença entre usar IA e comprimir assimetrias com IA. A maioria está fazendo o primeiro achando que está fazendo o segundo." | Thought leadership analítico |
| **Contrarian** | "A maioria dos analistas está olhando para o indicador errado." | Credibilidade técnica |
| **Dado específico** | "Taxa de default de PMEs subiu 23% em Q1. O mercado não precificou." | Credibilidade com dados |
| **Insight pessoal** | "Depois de 18 anos no mercado, aprendi que..." | Storytelling + autoridade |
| **Pergunta provocativa** | "Por que fundos com track record de 5 anos entregam menos alfa?" | Engagement reflexivo |
| **Promessa de framework** | "O framework que uso para avaliar risco de crédito em 3 etapas:" | Saves + educação |
| **Timestamp Transformation** | "2019: pedindo crédito pessoal para pagar contas. 2026: alocando capital em tese própria de AI." | Storytelling + autoridade, curiosity gap forte |
| **FOMO Insider** | "Estamos diante da maior assimetria desde 1999. Se você está vendo esse post, está à frente de 95% do mercado." | Oportunidade temporal, reach alto quando o tema é quente |

**Regras do hook:**
- Deve sinalizar explicitamente o tema (satisfaz audit semântico)
- Não pode ser clickbait (o sistema penaliza promessa ≠ entrega)
- Deve criar curiosity gap genuíno, não artificial
- Escreva o hook **por último** — após ter clareza do conteúdo completo

---

### Fórmula do Hook de Alto Alcance (validada empiricamente)

Análise comparativa de posts reais mostrou diferença de **14x no alcance** entre hooks com e sem tensão de identidade. Quatro padrões consistentemente superiores:

**Padrão 1 — Tensão de Identidade (maior alcance bruto):**

`[Palavra com duplo sentido ou carga emocional] + [de/dos + grupo específico]`

> Exemplo validado: *"A alucinação dos C-levels."* → 3.628 impressões
> Por que funciona: nomeia um grupo identificável, usa palavra que ativa dois sentidos simultaneamente (técnico + metafórico), faz o leitor se perguntar "sou eu?". Qualquer pessoa do grupo-alvo sente pressão de clicar.

Comparativo do mesmo criador, mesma semana:
- Hook com tensão de identidade + imagem: **3.628 impressões, 2.469 usuários**
- Hook informativo sem tensão (comentário de notícia): **256 impressões, 162 usuários**
- Newsletter como teaser + card: **223 impressões, 140 usuários**

**Padrão 2 — Distinção Analítica (ideal para voz analítica/thought leadership):**

`"Há uma diferença entre [X] e [Y]. A maioria está fazendo o primeiro acreditando que está fazendo o segundo."`

> Exemplo: *"Há uma diferença entre usar IA e comprimir assimetrias de informação com IA. A maioria das empresas está fazendo o primeiro e acreditando que está fazendo o segundo."*
> Por que funciona: cria tensão sem dramatismo, convida reflexão genuína, atrai comentários de pessoas que querem se diferenciar do grupo descrito. Ideal para perfis com voz analítica que evitam hipérbole.

**Padrão 3 — Timestamp Transformation (storytelling + autoridade):**

`[Ano]: [ponto baixo específico]`
`[Ano atual]: [ponto alto no mesmo domínio]`

> Exemplo: *"2019: liquidando posição na bolsa para manter a equipe paga. 2026: alocando pessoalmente em teses de AI infrastructure."*
> Por que funciona: dois timestamps geram um curiosity gap automático ("como?"). O leitor não precisa ser empurrado — ele mesmo se pergunta. Funciona porque o cérebro humano preenche arcos narrativos incompletos por default. Usar com moderação: só vale quando há transformação real e verificável.

**Padrão 4 — FOMO Insider (oportunidade temporal):**

`Estamos diante de [oportunidade grande com referência histórica]. Se você está vendo esse post, está à frente de [percentual] do [público].`

> Exemplo: *"Estamos diante da maior janela de reposicionamento de capital desde 2008. Se você está vendo esse post, está à frente de 95% dos alocadores brasileiros."*
> Por que funciona: ativa FOMO sem clickbait quando o tema é genuinamente relevante. A promessa precisa ser entregue no corpo — se não houver tese concreta, o algoritmo pune como hook enganoso. Ideal para posts sobre momentos de mercado reais.

**O que evitar nos hooks:**
- Afirmações paralelas que exigem processamento antes de gerar reação (ex: *"A NVIDIA criou X. Os LLMs criaram Y."* — interessante, mas não provoca ação imediata)
- Hooks puramente informativos sem tensão (*"A Anthropic lançou um modelo..."* — comentário de notícia, baixíssima autoridade percebida pelo algoritmo)
- Estruturas "Não X, mas Y" — soam como template e reduzem autenticidade percebida

---

### O Corpo

- Estrutura lógica: premissa → desenvolvimento → conclusão
- Parágrafos curtos (mobile-first: 72% do uso é mobile)
- Use white space estrategicamente — cada linha quebrada é uma micro-pausa de leitura
- Dados específicos ancoram credibilidade
- Perspectiva própria diferencia de conteúdo genérico
- 800-1.200 caracteres é o sweet spot para text posts (long-form tem 26% mais engajamento que posts curtos)

### O Encerramento

Evite "O que você pensa?" — é vago demais. Use CTAs orientados a ação ou perspectiva:

- "Qual dessas 3 variáveis você monitora mais de perto?"
- "Já passou por isso? Como resolveu?"
- "Discorda da minha leitura? Me convença."
- "Salva esse post — vai usar nas próximas reuniões de alocação."
- CTAs que nomeiam setores específicos geram respostas mais qualificadas e treinam o algoritmo sobre o público-alvo correto.

---

## Templates Persuasivos Validados

Templates são esqueletos narrativos comprovados. A lógica de Eugene Schwartz aplica: *"Copy is not written. Copy is assembled."* Use como skeleton, troque uma variável por vez e preserve a estrutura.

### Template 1 — PASTOR (Justin Welsh)

Framework persuasivo em 6 movimentos. É o mais versátil para posts que buscam converter atenção em lead ou ação concreta.

- **P**roblem — nomeie uma dor específica do leitor
- **A**mplify — mostre o custo de continuar ignorando
- **S**tory — aterrissar no seu próprio exemplo (sem dramatismo)
- **T**ransformation — descreva o estado após resolvido
- **O**ffer — apresente o recurso/insight/produto como ponte
- **R**esponse — um único próximo passo, claro

**Skeleton:**

```
Não há nada pior que [dor concreta].

E essa é a realidade de muitos [grupo]. Doloroso.

Eu lembro bem [momento específico em que você viveu isso].
[Detalhes: números, sensação, contexto].

Naquela época, [por que não havia saída fácil].

Hoje? [O que mudou na paisagem]:
- [Alternativa/opção 1]
- [Alternativa/opção 2]
- [Alternativa/opção 3]

[Frase otimista sobre a oportunidade].

[Reconheça uma dificuldade real do caminho].

Mas [reforce o benefício central].

Se você não sabe por onde começar, [primeiro passo simples].

[CTA único e concreto].
```

Quando usar: posts que empacotam uma oferta, recurso ou tese prática. Evitar para posts de pura reflexão — PASTOR pede desfecho acionável.

### Template 2 — Identity Upgrade

A premissa da Lara Acosta e Ali Abdaal: pessoas não compram produtos, compram **remédio para dor, resultado desejável e identidade nova**. Esse template trabalha os três antes de qualquer menção a oferta.

**Skeleton:**

```
Muitos [grupo/público] querem [resultado desejável].

Mas a maioria nunca [barreira invisível que trava].

[Identidade A] [comportamento default, limitante].
[Identidade B] [comportamento upgrade, que queremos sinalizar].

Se você quer [resultado desejável], [apresente recurso e como acessar].

[Imagem sugerida: comparativo de duas colunas, "Identidade A vs Identidade B"]
```

Quando usar: posts que promovem tese, metodologia ou framework proprietário. Funciona bem como carrossel de 2 slides (A vs B) ou imagem única.

### Template 3 — Advice I Ignored

Narrativa de hindsight. Converte erro em autoridade: você pagou o preço, o leitor não precisa pagar.

**Skeleton:**

```
Eu [reação dismissiva] com tanto conselho de [seu nicho].

(E hoje eu queria ter escutado.)

Quando comecei, todo mundo repetia:

"[Conselho comum #1]."
"[Conselho comum #2]."
"[Conselho comum #3]."

E eu pensava: tá, tá. Faço do meu jeito.

Fiz. [Liste 2-3 escolhas erradas/erros que cometeu].

Me custou.

O conselho que mais ignorei: "[frase do conselho que você ignorou]."

Eu achava que [por que dispensou]. Que [segundo motivo]. Que [terceiro motivo, o que acreditava no lugar].

Estava errado.

Os [clientes/empresas/profissionais] que vejo acertando hoje? [Breve descrição do que fazem]. Estão [fazendo o que você dispensou] há [período]. E funciona.

Porque [verdade humana que explica por que o conselho funciona].

[Resumo da lição central].

Eu só precisei aprender do jeito difícil.

[Pergunta para a audiência ou CTA].
```

Quando usar: posts de autoridade via vulnerabilidade. Funciona melhor em transições de carreira ou depois de marcos públicos (um lançamento, um deal anunciado, uma virada de tese).

---

## Processo de Escrita Rápida: Meat → Trailer → CTC

Framework de Justin Welsh (900M+ impressões). Inverte a ordem intuitiva de escrita para acelerar a produção sem sacrificar qualidade.

**1. Meat (conteúdo primeiro)**
Comece escrevendo o miolo: quais lições, erros, passos ou exemplos quer dividir? Escreva bruto, sem se preocupar com hook. É só despejar o valor.

**2. Trailer (hook depois)**
Com o conteúdo pronto, você enxerga qual é a "frase trailer" — a 1-3 primeiras linhas que capturam o que é mais intrigante do que você escreveu. Hook escrito por último é sempre mais honesto do que hook escrito primeiro.

**3. CTC (Call-to-Conversation)**
Encerre com resumo curto do insight central + pergunta que provoca diálogo específico (não o genérico "o que você acha?"). A pergunta deve nomear um contexto ou setor.

**Regra prática:** se você escreveu o hook antes do corpo, provavelmente o corpo vai "perseguir" o hook em vez de sustentá-lo. Inverta.

---

## Princípios de Produção Recorrente

Três regras de Lara Acosta (THE UK's #1 Female LinkedIn Creator, 325k seguidores em 4 anos) sobre o que sustenta produção de longo prazo.

**Repetição constrói reconhecimento.** Sua audiência não quer ideias frescas toda semana. Os criadores mais rentáveis repetem as mesmas 10-15 ideias validadas em 112 formas diferentes. O jogo não é originalidade — é distribuição. Ninguém vê tudo que você publica, e quem vê esquece em uma semana. Liste suas 10-15 teses centrais e rotacione ângulos.

**Genérico no hook, específico no corpo.** O reflexo natural é usar hook hiper-específico para filtrar o ICP. Erra. Hooks genéricos puxam volume; o ICP se auto-identifica no corpo quando você aprofunda. Quanto mais gente entra no funil, mais gente certa chega no fim.

**Uma variável por vez ao adaptar templates.** Quando copiar uma estrutura que deu certo, troque só o contexto. Não mexa em hook + estrutura + tom simultaneamente — você não vai saber o que funcionou e o que falhou. Reverse engineering rigoroso: pegue o esqueleto que viralizou, plugue sua ideia, mantenha todo o resto.

**Corolário sobre copiar criadores grandes:** não copie o stack completo de quem está em estágio mais avançado. Se seu objetivo é fechar call, coloque "Agenda uma call" no CTA. Não precisa de 10 lead magnets + newsletter + landing page só porque criadores top têm. Simplicidade ganha no início.

---

## Formatos e Performance

### Hierarquia de Formatos (2026)

**1. PDF Carousels (documento multi-slide)**
- Highest engagement: 6.6% médio (vs. 1-2% texto puro)
- Cada swipe = sinal de engajamento + dwell time
- 8-12 slides é o sweet spot
- Primeiro slide = hook visual
- Último slide = CTA ou pergunta
- Ideal para: frameworks, tutoriais, análises, checklists

**2. Text posts (longo)**
- Excelente para thought leadership e storytelling
- 800-1.200 caracteres performam melhor
- Estrutura em parágrafos curtos com line breaks
- Não inclua links no corpo (use comentários — mas cuidado com a "bridge penalty")

**3. Text + Imagem relevante**
- Padrão sólido para B2B
- Dados em imagem (charts, screenshots) são especialmente eficazes
- Foto pessoal/candid performa melhor que stock photo
- Imagem aumenta scroll-stop rate — sinal de engajamento registrado antes de qualquer clique

**4. Vídeo nativo curto**
- 30-90 segundos para builds de audiência
- Hook nos primeiros 3 segundos
- Legendas são obrigatórias
- Alcance crescendo 2x ano a ano, mas save-rate ainda abaixo de carousels

**5. Polls**
- 206% mais impressões que média
- Função: alcance (awareness) — não conversão
- Use para top of funnel e validação de tópicos

---

### Posts de Divulgação de Newsletter — Formato Correto

Posts que promovem uma newsletter (ou artigo) são sistematicamente penalizados quando formatados como **teaser + card**. O algoritmo lê o card de link como intenção de tráfego de saída e freia a distribuição antes mesmo de medir engajamento.

**O problema do formato teaser:**
- 3 linhas de texto introdutório + card da newsletter = sinal de "bridge behavior"
- O post não entrega valor autônomo → dwell time baixo → algoritmo freia
- Validado empiricamente: posts de newsletter como teaser tiveram alcance 16x menor que posts de thought leadership do mesmo criador

**O formato correto:**

```
[HOOK com tensão de identidade ou distinção analítica]

[ARGUMENTO COMPLETO no corpo — o post precisa ser valioso
para quem nunca vai clicar na newsletter]

[CTA reflexivo que convida comentários de setores específicos]

[card da newsletter — como bônus, não como destino]
```

**A regra prática:** escreva o post como se o card não existisse. Se o post não funciona de forma autônoma, reescreva antes de publicar. O leitor que não clica ainda deve ter consumido valor real — e esse consumo é o que o algoritmo mede.

---

## KPIs: O Que Medir Agora

Migre suas métricas de **reach para relevance**:

| Métrica Antiga | Métrica Nova | Por quê |
|----------------|-------------|---------|
| Impressões | Saves | Save = declaração de utilidade real |
| Likes | Profile visits de ICP | Qualidade do tráfego importa |
| Comentários (qtd) | DMs originados do post | Conversão real de atenção |
| Seguidores novos | Comment impressions | Você ganha reach nos comentários também |
| Reach total | Engagement de nicho | Relevância > volume |

O LinkedIn passou a mostrar também quantas pessoas **veem seus comentários** em outros posts — esse número frequentemente supera 2-3x as impressões dos próprios posts para comentadores ativos.

---

## Estratégia de Comentários

Comentar estrategicamente em posts de referências do seu nicho é uma das táticas mais subestimadas:

- Adiciona perspectiva real (não "Ótimo post!")
- Seu comentário fica visível para a audiência do creator — essencialmente "empréstimo de autoridade"
- O 360Brew usa seus comentários para treinar o modelo sobre quais conversas você pertence
- Comment impressions podem ser trackadas agora pelo LinkedIn

**Tell Them Theory:** além do comentário público, mande DM curto reconhecendo quem te marcou ou publicou algo que usou. A conversão em relacionamento real é muito maior via DM do que via comentário. E DMs gerados pelo seu engajamento sinalizam ao 360Brew que você é nó ativo no cluster — não apenas emissor.

### Priming de Algoritmo Pré-Publicação (15 dias)

Antes de publicar um post de reposicionamento semântico, comentar estrategicamente nos 15 dias anteriores acelera a formação do novo credibility cluster:

- **Dias 1-3:** Identificar 12-15 perfis do novo cluster. Observar sem comentar.
- **Dias 4-7:** 2 comentários/dia em posts dos Perfis A e B (founders + investidores do nicho).
- **Dias 8-12:** Adicionar Perfil C (analistas do tema). Subir para 3 comentários/dia.
- **Dias 13-15:** Reduzir para 1 comentário/dia — deixar o sinal assentar.

**Métricas de validação:** novos seguidores vindos do novo cluster (não do network histórico) e respostas substantivas de pessoas desconhecidas nos comentários.

---

## Workflow de Criação de Post

Quando o usuário pedir para criar um post:

1. **Identificar o pilar temático** — o post se encaixa em qual dos 2-3 temas do usuário?
2. **Definir o objetivo** — awareness (reach), educação (saves), conversão (DMs)?
3. **Escolher o formato** — texto, carousel, vídeo, poll?
4. **Escrever o Meat primeiro** — despejar o conteúdo bruto, sem hook
5. **Escolher template persuasivo** — PASTOR, Identity Upgrade, Advice I Ignored ou estrutura livre
6. **Escrever o hook (Trailer) por último** — preferir Tensão de Identidade, Distinção Analítica, Timestamp Transformation ou FOMO Insider
7. **Verificar alinhamento semântico** — o vocabulário do post espelha o headline/About do perfil?
8. **Checar o CTC** — nomeia setor ou grupo específico para atrair comentários qualificados?
9. **Revisar o "Lost in Distance"** — as primeiras 2 frases entregam o sinal temático correto?

---

## Workflow de Revisão de Post Existente

Quando o usuário trouxer um post para revisar:

1. Analisar se o hook está nos primeiros 210 caracteres e usa um dos 4 padrões validados
2. Verificar se o tema é explícito (satisfaz audit semântico do 360Brew)
3. Checar estrutura lógica: premissa → desenvolvimento → conclusão (ou um dos templates validados)
4. Se for post de newsletter: verificar se o corpo entrega argumento completo (não teaser)
5. Identificar se há engagement bait ou hashtag stuffing para remover
6. Avaliar se o CTC provoca reflexão ou é genérico demais
7. Checar se a voz é autêntica ou soa como template de IA
8. Se o post está copiando estrutura de outro criador, confirmar que só uma variável foi alterada

---

## IP Branding: Construindo Frameworks Proprietários

O 360Brew amplia conteúdo que demonstra **expertise única**. Criar frameworks com nomes próprios é uma das estratégias mais eficazes:

- James Clear transformou "formação de hábitos" em *Atomic Habits* (1% improvements)
- Simon Sinek transformou "liderança com propósito" em *Start With Why*
- A lógica: frameworks são mais memoráveis, mais compartilháveis e mais "saveable"

Frameworks permitem criar conteúdo consistente sem depender de storytelling vulnerável ou eventos do dia.

---

## Notas de Implementação

- **Tempo para resultado:** ~90 dias de posting consistente e alinhado para o sistema construir o credibility cluster
- **Frequência ideal:** 1-2 posts de alta qualidade por semana superam posting diário
- **Primeiros 60 minutos:** Responder comentários logo após publicação ainda importa — gera engagement velocity inicial
- **Links externos:** Se necessário, coloque nos comentários — mas o sistema detecta "bridge behavior", então o conteúdo nativo precisa ter valor real independente
- **Company pages:** Alcance orgânico caiu muito mais para páginas. Employee advocacy coordenada (comentários de especialistas internos) compensa
- **Reposicionamento semântico:** Primeiros posts após mudança de nicho performam abaixo da média histórica. Use o plano de priming de 15 dias antes de publicar o post de reposicionamento.
- **Content Creative Fit:** vídeo nativo performa bem em 2026, mas não force formato em que você é ruim. Creator que odeia câmera fazendo vídeo ruim gera save-rate pior que o mesmo creator em texto bem escrito. Encontre o formato em que você é naturalmente forte e otimize ele.
