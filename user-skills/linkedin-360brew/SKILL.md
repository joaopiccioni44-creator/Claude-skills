---
name: linkedin-360brew
description: >
  Skill principal de LinkedIn alinhada ao algoritmo 360Brew (2025-2026). Use sempre
  que o usuário mencionar LinkedIn, posts, alcance, impressões, saves, dwell time,
  thought leadership, personal branding, growth ou estratégia geral de conteúdo
  na plataforma. Esta skill é o núcleo conceitual do sistema 360Brew e o roteador
  para skills satélites mais profundas (linkedin-hooks, linkedin-post-doctor,
  linkedin-carousel, linkedin-newsletter-bridge, linkedin-voice-joao,
  linkedin-profile, linkedin-templates, linkedin-mix, linkedin-engajamento,
  linkedin-deplatforming, linkedin-repurposing, linkedin-frameworks-ip).
  Carregue as satélites quando o trabalho exigir profundidade específica.
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

## O que o 360Brew Recompensa vs. Penaliza

**Recompensa:** expertise real, opiniões fundamentadas, estrutura lógica argumentativa, conteúdo "save-worthy" (frameworks, dados, checklists), comentários substantivos no nicho, voz autêntica (credibility scoring detecta IA genérica), perguntas que provocam reflexão real.

**Penaliza:** engagement bait gamificado ("Comente FIRE para receber"), engagement pods, conteúdo genérico de IA, hashtag stuffing (hashtags não influenciam mais distribuição semântica), tagging massivo, links externos no corpo (off-platform behavior), alta frequência com baixa qualidade, posts de newsletter como teaser+card (bridge penalty).

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

## Estrutura Base de um Post

```
[HOOK — 210 caracteres máximo antes do "Ver mais"]

[CORPO — desenvolvimento com estrutura lógica]

[ENCERRAMENTO — CTA reflexivo ou convite a perspectiva]
```

Hook recebe 3-5x mais atenção do modelo (fenômeno Lost in Distance). Corpo no sweet spot 800-1.200 caracteres, parágrafos curtos para mobile (72% do uso), perspectiva própria como diferencial. Encerramento evita "O que você pensa?" e prefere CTAs que nomeiam setor ou grupo específico.

---

## Mapa de Roteamento — Qual Skill Usar Para Cada Job

Esta skill é o núcleo conceitual e estratégico. Para trabalho profundo, ative a skill satélite correspondente:

| Job | Skill a usar | Quando |
|---|---|---|
| Criar, propor ou revisar hook | **`linkedin-hooks`** | Sempre que envolver os primeiros 210 chars; consulta o tracker antes de propor |
| Revisar / diagnosticar post pronto | **`linkedin-post-doctor`** | Post escrito que precisa de checklist de qualidade |
| Construir carrossel (PDF multi-slide) | **`linkedin-carousel`** | Output é carrossel de 8-12 slides |
| Divulgar newsletter sem matar alcance | **`linkedin-newsletter-bridge`** | Post que referencia/promove newsletter ou artigo externo |
| Calibrar voz autoral do João | **`linkedin-voice-joao`** | Filtro final contra "Claude genérico" |
| Otimizar headline / About / Featured / Experience | **`linkedin-profile`** | Workstream de perfil — positioning, ICP, Authority Triangle |
| Aplicar template persuasivo | **`linkedin-templates`** | Quando o post pede skeleton (PASTOR, Identity Upgrade, Advice I Ignored) |
| Definir mix saudável de tipos de post | **`linkedin-mix`** | Decidir 50/25/15/10, auditar mix mensal |
| Estratégia de comentários e priming pré-publicação | **`linkedin-engajamento`** | Engajar 30/30/30/10, plano de 15 dias |
| Construir lista de email e audiência própria | **`linkedin-deplatforming`** | Lead magnet, funil de email, newsletter |
| Adaptar conteúdo cross-platform | **`linkedin-repurposing`** | Reaproveitar para Instagram, X, newsletter, vídeo |
| Construir framework proprietário com nome | **`linkedin-frameworks-ip`** | Criar IPs no estilo Atomic Habits / Start With Why |

Quando o usuário pedir um post completo, o pipeline natural é: definir pilar e tipo (`linkedin-mix`) → escrever Meat (corpo) → escolher template (`linkedin-templates`) → ativar `linkedin-hooks` para o gancho → ativar `linkedin-voice-joao` como filtro final → opcional `linkedin-post-doctor` antes de publicar.

> Enquanto as satélites não existirem, o conteúdo completo está preservado em `_pre-refactor-backup.md` no diretório desta skill — recorra a ele se precisar de profundidade que ainda não foi migrada.

---

## Princípios Operacionais

**Pilares do João (memória do projeto LinkedIn & Instagram):** AI e transformação tecnológica, mercados financeiros e análise macro, thought leadership para empreendedores/líderes. Posicionamento recorrente: *practitioner-turned-builder* — institutional credibility cruzando para AI-native startup. Brands ativos: Capital Pulse (newsletter hub), PulseInvest.ai (plataforma de portfólios AI), Exército de Agentes (infra interna).

**Tempo para resultado:** ~90 dias de posting consistente e alinhado para o sistema construir o credibility cluster.

**Frequência ideal:** 1-2 posts de alta qualidade por semana superam posting diário com qualidade média.

**Primeiros 60 minutos:** Responder comentários logo após publicação gera engagement velocity inicial.

**Links externos:** Se necessários, vão nos comentários — mas o sistema detecta bridge behavior. O conteúdo nativo precisa ter valor real independente.

**Reposicionamento semântico:** Primeiros posts após mudança de nicho performam abaixo da média histórica. Use o plano de priming de 15 dias antes de publicar o post de reposicionamento (detalhado em `linkedin-engajamento`).

**Content Creative Fit:** Não force formato em que você é ruim. Creator que odeia câmera fazendo vídeo ruim gera save-rate pior que o mesmo creator em texto bem escrito.

**Email > followers no longo prazo:** Followers é métrica da plataforma; email é métrica sua. Detalhes em `linkedin-deplatforming`.

---

## Workflow Genérico de Criação

1. Identificar o pilar temático (qual dos 2-3 temas?)
2. Identificar o tipo de post no mix → ativar `linkedin-mix` se houver dúvida
3. Escolher o formato (texto, carrossel, vídeo, poll) — carrossel ativa `linkedin-carousel`
4. Escrever o Meat (corpo) primeiro, sem se preocupar com hook
5. Acionar `linkedin-templates` se a estrutura pedir skeleton validado
6. Acionar `linkedin-hooks` para gerar/escolher o gancho (sempre por último)
7. Verificar alinhamento semântico com headline/About do perfil
8. Acionar `linkedin-voice-joao` como filtro final
9. Opcional: rodar `linkedin-post-doctor` para diagnóstico

## Workflow Genérico de Revisão

Para revisão sistemática, ative diretamente `linkedin-post-doctor` — ela traz o checklist completo. Esta skill core foca em estratégia e roteamento.
