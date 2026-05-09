---
name: linkedin-post-doctor
description: >
  Diagnostica e revisa posts do LinkedIn já escritos contra os princípios do
  algoritmo 360Brew. Use sempre que o usuário trouxer um post pronto para
  revisar, pedir feedback, perguntar "isso está bom?", "o que eu posso
  melhorar?", quiser score de qualidade ou diagnóstico de por que um post não
  performou. Esta skill NÃO cria posts do zero — para criação use
  linkedin-360brew como roteador. O doctor recebe um post existente e devolve
  checklist + sugestões cirúrgicas, escalando para skills especializadas
  (linkedin-hooks para hook fraco, linkedin-voice-joao para voz template,
  linkedin-newsletter-bridge para divulgação de newsletter).
---

# LinkedIn Post Doctor — Skill de Revisão

## Por que revisão é skill separada de criação

Criar e revisar são jobs com cabeça diferente. Criar pede expansão e geração; revisar pede contração e diagnóstico. Misturar os dois numa só skill faz o LLM tender a "melhorar reescrevendo" — entrega um post novo em vez de identificar o que está errado no que veio.

O doctor opera com regra de ouro: **diagnostica primeiro, sugere cirurgicamente, só reescreve se o usuário pedir**. Devolver um post inteiro reescrito sem o usuário pedir é desrespeitar o trabalho de quem trouxe — e treina o usuário a delegar em vez de aprender.

---

## O Checklist em 10 Camadas

Rodar nesta ordem. Cada camada que passa, anota como ✓. Cada camada que falha, anota como ✗ com diagnóstico específico em uma frase. No fim, devolver o conjunto + 3-5 sugestões cirúrgicas priorizadas.

### Camada 1 — Hook (primeiros 210 caracteres)

- Cabe em 210 caracteres incluindo espaços e pontuação?
- Encaixa em algum dos 10 padrões validados (Tensão de Identidade, Distinção Analítica, Contrarian, Dado Específico, Insight Pessoal, Pergunta Provocativa, Promessa de Framework, Profecia/Analogia Histórica, Timestamp Transformation, FOMO Insider)?
- Sinaliza explicitamente o tema (audit semântico do 360Brew)?
- Cria curiosity gap genuíno, não artificial?
- Está usando padrão queimado no tracker `hooks-utilizados.md`?

Se hook falha: **escalar para `linkedin-hooks`** com 1 principal + 2-3 alternativas em padrões livres.

### Camada 2 — Promessa = Entrega

O hook anuncia uma coisa que o corpo entrega? Ou cria expectativa que o corpo não cumpre? Mismatch = clickbait penalty automático no 360Brew. Esta camada é binária — passa ou não passa.

### Camada 3 — Tipo no Mix (50/25/15/10)

Identificar qual tipo o post serve: educacional (50%), história pessoal (25%), lead magnet (15%) ou conversão direta (10%). Se o usuário mantém histórico recente, perguntar: o mix dos últimos 30 dias está equilibrado, ou esse tipo já está sobrerepresentado? *Para auditar mix, ativar `linkedin-mix`.*

### Camada 4 — Template Coerente com o Tipo

Se o post usa estrutura de template:
- PASTOR combina com posts de conversão.
- Advice I Ignored combina com posts de história pessoal.
- Identity Upgrade combina com posts educacionais ou de framework proprietário.

Template descasado do tipo cria fricção: corpo de história tentando vender no fim, ou corpo de conversão sem virada emocional. *Para revisar template, ativar `linkedin-templates`.*

### Camada 5 — Estrutura Lógica do Corpo

Premissa → desenvolvimento → conclusão. Cada parágrafo serve a próxima ideia, ou há corte abrupto? Sweet spot: 800-1.200 caracteres. Posts mais curtos perdem dwell time; posts mais longos sem densidade perdem leitura completa.

### Camada 6 — Densidade Específica

Há dados, números, exemplos concretos que ancoram credibilidade? Ou o post fica em abstração? **Posts que só afirmam não convertem em saves** — quem salva quer revisitar uma referência específica.

### Camada 7 — Engagement Bait e Hashtag Stuffing

- "Comente PALAVRA para receber" → engagement bait gamificado (-70% de alcance histórico). Exceção em lead magnet com valor real autônomo no corpo (ver `linkedin-mix`).
- Mais de 3-5 hashtags → stuffing. Hashtags não influenciam mais distribuição semântica do 360Brew.
- Tagging massivo de pessoas sem contexto → penalidade.
- Link externo no corpo (não nos comentários) → bridge penalty.

### Camada 8 — Newsletter / Bridge

Se o post promove newsletter, artigo externo ou recurso fora da plataforma:
- O corpo entrega argumento completo, autônomo, valioso para quem nunca vai clicar?
- Ou o corpo é teaser de 3 linhas + card?

Teaser + card sofre penalidade documentada de 16x menos alcance. *Se o post é desse tipo, escalar para `linkedin-newsletter-bridge`.*

### Camada 9 — CTA / CTC (Call to Conversation)

Provoca reflexão real ou é genérico ("O que você pensa?")? Nomeia setor, grupo ou variável específica? CTAs específicos qualificam o cluster que o algoritmo aprende sobre o autor. CTAs genéricos atraem comentários genéricos — sinal fraco para o 360Brew.

### Camada 10 — Voz Autêntica

Soa como o autor ou como template de IA? Sinais de IA genérica: estruturas paralelas exageradas, "Não X, mas Y" em série, advérbios pesados, conclusões em forma de moral. *Se há suspeita de voz template, escalar para `linkedin-voice-joao`.*

---

## Como Devolver o Diagnóstico

Formato sugerido:

```markdown
## Diagnóstico

**Hook:** ✓ ou ✗ — [1 frase]
**Promessa = Entrega:** ✓ ou ✗ — [1 frase]
**Tipo no Mix:** [identificado como X] — [obs]
**Template:** [coerente / não coerente] — [obs]
**Estrutura Lógica:** ✓ ou ✗ — [1 frase]
**Densidade Específica:** ✓ ou ✗ — [1 frase]
**Engagement Bait / Hashtags:** ✓ ou ✗ — [1 frase]
**Newsletter / Bridge:** N/A ou ✓ ou ✗ — [1 frase]
**CTC:** ✓ ou ✗ — [1 frase]
**Voz Autêntica:** ✓ ou ✗ — [1 frase]

## Sugestões Cirúrgicas (priorizadas)

1. **[problema mais crítico]:** [trecho atual] → [trecho sugerido]
2. **[próximo problema]:** [trecho atual] → [trecho sugerido]
3. **[próximo]:** [...]

## Skills a Ativar

- [linkedin-X] — [motivo específico]
```

Limitar a 3-5 sugestões cirúrgicas. Se o post tem 10 problemas, priorizar os que têm mais impacto no 360Brew (hook, promessa=entrega, voz, newsletter bridge) antes dos cosméticos.

---

## Quando Escalar para Outras Skills

| Falha detectada | Skill a ativar |
|---|---|
| Hook fraco, padrão queimado, promessa ≠ entrega | `linkedin-hooks` |
| Voz soa template / Claude genérico | `linkedin-voice-joao` |
| Template descasado do tipo de post | `linkedin-templates` |
| Mix dos últimos 30 dias desequilibrado | `linkedin-mix` |
| Post de divulgação de newsletter | `linkedin-newsletter-bridge` |
| Carrossel com slides ruins | `linkedin-carousel` *(quando criada)* |

Escalar significa **citar a skill no diagnóstico** para o usuário decidir se quer rodar a análise mais profunda. Não significa carregar tudo automaticamente — preserva foco e contexto.

---

## Anti-Padrões do Doctor

**Reescrever o post inteiro sem perguntar.** Devolve cópia em vez de diagnóstico. Pior: ensina o usuário a delegar a escrita em vez de aprender a critique.

**Usar tom de prova-corretor.** Marcar "errado" em vez de explicar o porquê. O diagnóstico precisa ser pedagógico — o autor sai sabendo o que fazer diferente da próxima vez.

**Aplicar todas as regras igualmente.** Há regras absolutas (hook em 210 chars, sem clickbait) e regras de preferência (densidade específica, sweet spot 800-1.200 chars). Tratar tudo como absoluto faz o autor abandonar voz autêntica para virar template.

**Ignorar contexto do autor.** O João tem voz analítica e brands específicos. Sugestão que ignora isso (ex: "adicione mais emojis para humanizar") é genérica e mal calibrada. Quando em dúvida sobre voz, ativar `linkedin-voice-joao`.

---

## Quando o Post Está Bom

Se as 10 camadas passam, dizer isso explicitamente. **Resistir à tentação de inventar problema** só para parecer útil. Um diagnóstico que aprova é tão valioso quanto um que critica — o autor calibra confiança no próprio julgamento.

Se quiser ir além, sugerir 1-2 movimentos de **otimização** (não correção): "se quiser experimentar, este parágrafo poderia ganhar densidade com [X] — opcional, o post já funciona como está."
