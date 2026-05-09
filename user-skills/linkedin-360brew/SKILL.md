---
name: linkedin-360brew
description: >
  Skill principal de LinkedIn alinhada ao algoritmo 360Brew (2025-2026) e
  calibrada com o Q1 2026 State of the Algorithm Report (397.605 posts
  analisados). Use sempre que o usuário mencionar LinkedIn, posts, alcance,
  impressões, saves, dwell time, thought leadership, personal branding, growth
  ou estratégia geral de conteúdo na plataforma. Esta skill é o núcleo
  conceitual do sistema 360Brew e o roteador para skills satélites mais
  profundas (linkedin-hooks, linkedin-post-doctor, linkedin-carousel,
  linkedin-newsletter-bridge, linkedin-voice-joao, linkedin-profile,
  linkedin-templates, linkedin-mix, linkedin-engajamento, linkedin-deplatforming,
  linkedin-repurposing, linkedin-frameworks-ip). Carregue as satélites quando
  o trabalho exigir profundidade específica.
---

# LinkedIn 360Brew — Núcleo Conceitual e Roteador

## O que é o 360Brew

O **360Brew** é o foundation model de 150 bilhões de parâmetros (arquitetura Mixtral 8x22, MoE) que substituiu todos os sistemas de ranking do LinkedIn. Publicado no arXiv em janeiro de 2025, está em pleno deployment desde o início de 2026.

A mudança filosófica central é simples e poderosa: o sistema antigo media *o que você postava*; o novo mede *quem você é*. Para cada potencial viewer, o modelo constrói um prompt em linguagem natural e se pergunta: *"Dado quem essa pessoa é e o que engajou recentemente, esse post vai gerar valor real para ela?"*

---

## Os 5 Pilares do 360Brew

**1. Alinhamento Perfil ↔ Conteúdo (Semantic Identity).** O 360Brew lê perfil e posts como um documento semântico unificado. Headline, About, Skills e Featured precisam compartilhar vocabulário com os posts. Mismatch = distribuição limitada. *Profundidade em `linkedin-profile`.*

**2. Consistência Temática (Topic Authority).** O sistema constrói um credibility cluster em torno de quem você é. Leva ~90 dias de posting consistente para se estabelecer. Regra 80/20: 80% dos posts dentro de 2-3 pilares definidos. Topic hopping dilui autoridade em todos os temas.

**3. Depth Score.** Save vale 5-10x mais que like. DM originado do post é o sinal mais forte. Comment com perspectiva própria e dwell time são altos. Comment genérico ("Ótimo post!") é quase nulo ou negativo. **Clickbait penalty:** clicar em "Ver mais" e abandonar em segundos é registrado como sinal negativo.

**4. In-Context Learning (ICL).** O modelo aprende em tempo real sobre cada viewer. Os comentários que você atrai treinam o algoritmo sobre quem é seu público — CTAs que nomeiam setores específicos qualificam o cluster.

**5. Multi-Surface Distribution.** O modelo opera em feed, busca, notificações, newsletters e "People You May Know" simultaneamente. Posts de alta qualidade podem ser reativados 4-7 dias após publicação se atingirem novos thresholds.

---

## O Estado da Plataforma em Q1 2026

Dados do report Q1 2026 baseados em 397.605 posts analisados:

- **Median impressions caíram 68%** desde o pico de 2023; Q1 2026 ainda registrou queda de 2% versus Q4 2025.
- **Gap de 124x** entre o reach do top 1% e o reach médio. Posts virais têm teto mais baixo, mas a vantagem do top é maior.
- **Bottom 80% dos posts** de creators médios geram apenas 11% das impressões totais. A consistência sozinha não basta — o que importa é qual percentual dos seus posts são de fato bons.
- **Career Development** é a categoria mais viral: posts dessa categoria têm **2.5x mais probabilidade de viralizar** que qualquer outra. Para o João, isso conecta diretamente com a narrativa *practitioner-turned-builder*.
- **Top 1% creators respondem 255% mais comentários** que a média (134 replies/semana vs 38). Engagement de execs do ICP vale mais que volume.

---

## O que o 360Brew Recompensa vs. Penaliza

**Recompensa:** expertise real, opiniões fundamentadas, estrutura lógica argumentativa, conteúdo "save-worthy" (frameworks, dados, checklists), comentários substantivos no nicho, voz autêntica (credibility scoring detecta IA genérica), perguntas específicas que provocam reflexão real, **links externos de valor curatorial (1-3 links = +43% reach; >3 links = +441%)**, **emojis seletivos em headings e CTAs (+370% reach quando bem usados)**.

**Penaliza:** engagement bait gamificado ("Comente FIRE para receber"), engagement pods, conteúdo genérico de IA, **hashtag stuffing (>3 hashtags = -71% reach; ideal é zero)**, tagging massivo, alta frequência com baixa qualidade, posts de newsletter como teaser+card sem valor autônomo (bridge penalty — ver `linkedin-newsletter-bridge`), **linguagem complexa (palavras médias >5 letras = -40% performance; alvo é grade 5-7 reading level)**, perguntas finais genéricas (reduzem reach a 853 vs 1.140 sem pergunta nenhuma).

> **Mudança importante de regra:** a versão anterior dessa skill dizia "links externos no corpo penalizam". O Q1 2026 report contradiz frontalmente — links de valor real são premiados. A premissa é "high-value content wins despite links". Para divulgação de newsletter, ainda vale a regra de teaser+card (`linkedin-newsletter-bridge`); a regra mudada se aplica a links curatoriais que agregam ao argumento do post.

---

## KPIs: Reach → Relevance

| Métrica Antiga | Métrica Nova | Por quê |
|---|---|---|
| Impressões | Saves | Save = declaração de utilidade real |
| Likes | Profile visits de ICP | Qualidade do tráfego importa |
| Comentários (qtd) | DMs originados do post | Conversão real de atenção |
| Seguidores novos | Comment impressions | Ganho de reach nos comentários |
| Reach total | Engagement de nicho | Relevância > volume |
| — | Email subscribers de lead magnets | Audiência que você efetivamente possui |

O LinkedIn passou a mostrar quantas pessoas veem seus comentários em outros posts — frequentemente supera 2-3x as impressões dos próprios posts para comentadores ativos.

---

## Estrutura de 6 Seções (Adotada do Q1 2026)

A estrutura ideal de um post forte tem seis seções, cada uma com função clara. Esta é a base operacional: todo post deveria atravessar essas seis (alguns templates como PASTOR ou Identity Upgrade já implementam essa lógica de forma diferente).

1. **Hook** — primeiras 1-3 linhas. Deve parar o scroll. Três qualidades de hook forte: surpreender, nomear um problema sentido pelo leitor, ou prometer recompensa específica. Para profundidade, ativar `linkedin-hooks`.
2. **Pain Points** — nomeia o problema específico que o leitor está vivendo. Quanto mais preciso ("você passou três horas escrevendo um post que rendeu doze likes de amigos"), mais o leitor se sente visto.
3. **Actionable Value** — ensina algo concreto que o leitor pode aplicar nas próximas 24h. Evitar conselho vago ("seja autêntico"); preferir tática específica ("abra todo post com frase abaixo de dez palavras").
4. **Dream Picture** — pinta como a vida ou o trabalho ficam depois de aplicar a tática. Tangibilizar a recompensa muda o foco do leitor de "trabalho" para "ganho".
5. **Engagement Question** — uma pergunta específica que convida resposta real, fácil de responder em uma frase. Evita o genérico "o que você acha?".
6. **CTA** — uma única ação clara (seguir, salvar, repostar). Não empilhar três CTAs.

### Algorithm Health Check (números quantitativos)

Independente da estrutura de 6 seções, todo post pode ser auditado por estes números do Q1 2026:

| Dimensão | Alvo | Penalidade se desviar |
|---|---|---|
| Length | 1.250-3.000 caracteres (peak >2.500 = 1.862 median impressions) | Posts curtos perdem dwell time; muito longos sem densidade perdem leitura completa |
| Parágrafos | 14+ parágrafos curtos | <7 parágrafos = -66% performance |
| Hashtags | Zero (ou no máximo 1-2 ultra-relevantes) | >3 hashtags = -71% reach |
| Emojis | Seletivos em headings/CTAs (🚨 ✅ ❌ 💸 📈) | +370% reach quando bem usados; overuse soa amador |
| Links externos | 1-3 links de valor curatorial no corpo | Sem links quando agregam = oportunidade perdida; lembrando que regra de teaser+card de newsletter continua valendo |
| Closing question | Genuína e específica, ou statement provocativo | Pergunta genérica = 853 impressões médias vs 1.140 sem pergunta nenhuma |
| Word complexity | Grade 5-7 reading level; palavras médias ≤5 letras | >5 letras médias = -40% performance |

Para revisão sistemática contra estes números, ativar `linkedin-post-doctor` — traz o scoring /60 + Algorithm Health Check formalizados.

---

## Mapa de Roteamento — Qual Skill Usar Para Cada Job

Esta skill é o núcleo conceitual e estratégico. Para trabalho profundo, ative a skill satélite correspondente:

| Job | Skill a usar | Quando |
|---|---|---|
| Criar, propor ou revisar hook | **`linkedin-hooks`** | Sempre que envolver as primeiras 1-3 linhas; consulta o tracker antes de propor |
| Revisar / diagnosticar post pronto (scoring /60) | **`linkedin-post-doctor`** | Post escrito que precisa de avaliação por seção + Algorithm Health Check |
| Construir carrossel (PDF multi-slide) | **`linkedin-carousel`** | Output é carrossel; lembrando que infographics = 29% dos top 1% |
| Divulgar newsletter sem matar alcance | **`linkedin-newsletter-bridge`** | Post que referencia/promove newsletter ou artigo externo (regra teaser+card vale aqui) |
| Calibrar voz autoral + filtrar AI tells | **`linkedin-voice-joao`** | Filtro final em qualquer texto (LinkedIn, newsletter, copy) — codifica fingerprint do João + 50+ padrões anti-AI universais |
| Otimizar headline / About / Featured / Experience | **`linkedin-profile`** | Workstream de perfil — positioning, ICP, Authority Triangle |
| Aplicar template persuasivo | **`linkedin-templates`** | Quando o post pede skeleton (PASTOR, Identity Upgrade, Advice I Ignored) |
| Definir mix saudável de tipos de post | **`linkedin-mix`** | Decidir 50/25/15/10, auditar mix mensal |
| Estratégia de comentários e priming pré-publicação | **`linkedin-engajamento`** | Engajar 30/30/30/10, plano de 15 dias |
| Construir lista de email e audiência própria | **`linkedin-deplatforming`** | Lead magnet, funil de email, newsletter |
| Adaptar conteúdo cross-platform | **`linkedin-repurposing`** | Reaproveitar para Instagram, X, newsletter, vídeo |
| Construir framework proprietário com nome | **`linkedin-frameworks-ip`** | Criar IPs no estilo Atomic Habits / Start With Why |

Quando o usuário pedir um post completo, o pipeline natural é: definir pilar e tipo (`linkedin-mix`) → escrever as 6 seções (`linkedin-templates` se quiser skeleton) → ativar `linkedin-hooks` para o gancho → ativar `linkedin-voice-joao` como filtro final → opcional `linkedin-post-doctor` para diagnóstico antes de publicar.

> Enquanto as satélites `linkedin-carousel`, `linkedin-newsletter-bridge`, `linkedin-profile`, `linkedin-engajamento`, `linkedin-deplatforming`, `linkedin-repurposing`, `linkedin-frameworks-ip` não existirem, o conteúdo completo está preservado em `_pre-refactor-backup.md` no diretório desta skill — recorra a ele se precisar de profundidade que ainda não foi migrada.

---

## Princípios Operacionais

**Pilares do João (memória do projeto LinkedIn & Instagram):** AI e transformação tecnológica, mercados financeiros e análise macro, thought leadership para empreendedores/líderes. Posicionamento recorrente: *practitioner-turned-builder* — institutional credibility cruzando para AI-native startup. Brands ativos: Capital Pulse (newsletter hub), PulseInvest.ai (plataforma de portfólios AI), Exército de Agentes (infra interna). **Career Development é categoria adjacente natural** — a transição de carreira é tese viral e ativa identificação imediata em quem está em ponto similar de virada.

**Tempo para resultado:** ~90 dias de posting consistente e alinhado para o sistema construir o credibility cluster.

**Frequência ideal:** 1-2 posts de alta qualidade por semana superam posting diário com qualidade média. Posting mais que 1x/dia só compensa se a qualidade se mantém.

**Primeiros 60 minutos:** Responder comentários logo após publicação gera engagement velocity inicial. **Top 1% creators respondem 255% mais que a média** — esse hábito sozinho já é diferencial.

**Timing de publicação:** janela 11AM-1PM GMT (8h-10h Brasília) tem melhor engagement médio (~1.900 impressões). Evitar 4PM-1AM GMT (~500-750). Mais importante que isso: postar quando teu ICP está online.

**Links externos:** se agregam valor curatorial real, vão no corpo (1-3 links = +43% reach; >3 = +441%). Se forem só promo de newsletter sem valor próprio, sofrem bridge penalty — regra teaser+card continua valendo (`linkedin-newsletter-bridge`).

**Reposicionamento semântico:** Primeiros posts após mudança de nicho performam abaixo da média histórica. Use o plano de priming de 15 dias antes de publicar o post de reposicionamento (detalhado em `linkedin-engajamento`).

**Content Creative Fit:** Não force formato em que você é ruim. Creator que odeia câmera fazendo vídeo ruim gera save-rate pior que o mesmo creator em texto bem escrito.

**Email > followers no longo prazo:** Followers é métrica da plataforma; email é métrica sua. Detalhes em `linkedin-deplatforming`.

---

## Hierarquia de Formatos (Q1 2026)

| Formato | Performance | Notas |
|---|---|---|
| Infographics | 29% dos top 1% posts; ~3.0x reach vs text post | Maior categoria viral em 2026; AI-generated infographics dominando |
| Carousels | ~3.0x reach vs text post | Cada swipe = sinal de engajamento + dwell time |
| Text + Imagem portrait | Portrait +47% vs landscape (1200x1500px / 4:5) | Padrão sólido para B2B; foto pessoal supera stock |
| Text post longo | Sweet spot 1.250-3.000 chars | Excelente para thought leadership; sem tipo visual perde scroll-stop |
| Vídeo horizontal | +18% vs vídeo vertical | LinkedIn é uso no trabalho — vertical desconforta socialmente |
| Polls | 206% mais impressões que média | Awareness, não conversão |

---

## Workflow Genérico de Criação

1. Identificar o pilar temático (qual dos 2-3 temas?)
2. Identificar o tipo de post no mix → ativar `linkedin-mix` se houver dúvida
3. Escolher o formato (texto, carrossel, vídeo, poll) — carrossel ativa `linkedin-carousel`
4. Escrever o Meat (corpo) primeiro nas 6 seções, sem se preocupar com hook
5. Acionar `linkedin-templates` se a estrutura pedir skeleton validado (PASTOR, Identity Upgrade, Advice I Ignored)
6. Acionar `linkedin-hooks` para gerar/escolher o gancho (sempre por último; consulta tracker)
7. Verificar alinhamento semântico com headline/About do perfil
8. Acionar `linkedin-voice-joao` como filtro final (calibração + anti-AI tells)
9. Opcional: rodar `linkedin-post-doctor` para scoring /60 + Algorithm Health Check antes de publicar

## Workflow Genérico de Revisão

Para revisão sistemática, ative diretamente `linkedin-post-doctor` — ela traz o sistema de scoring /60 em 6 seções + Algorithm Health Check. Esta skill core foca em estratégia e roteamento.
