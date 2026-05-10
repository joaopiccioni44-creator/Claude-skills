---
name: linkedin-post-doctor
description: >
  Diagnostica e revisa posts do LinkedIn já escritos contra os princípios do
  algoritmo 360Brew e os dados do Q1 2026 State of the Algorithm Report. Aplica
  sistema de scoring /60 em 6 seções (Hook, Pain Points, Actionable Value,
  Dream Picture, Engagement Question, CTA) + Algorithm Health Check
  quantitativo (length, parágrafos, hashtags, emojis, links, word complexity).
  Use sempre que o usuário trouxer um post pronto para revisar, pedir feedback,
  perguntar "isso está bom?", "qual o score?", "o que posso melhorar?", ou
  quiser diagnóstico de por que um post não performou. Esta skill NÃO cria
  posts — para criação use linkedin-360brew como roteador. O doctor recebe um
  post existente e devolve scoring + Algorithm Health Check + sugestões
  cirúrgicas, escalando para skills especializadas conforme falha.
---

# LinkedIn Post Doctor — Skill de Revisão e Scoring

## Por que revisão é skill separada de criação

Criar e revisar são jobs com cabeça diferente. Criar pede expansão e geração; revisar pede contração e diagnóstico. Misturar os dois numa só skill faz o LLM tender a "melhorar reescrevendo" — entrega um post novo em vez de identificar o que está errado no que veio.

O doctor opera com regra de ouro: **diagnostica primeiro, sugere cirurgicamente, só reescreve se o usuário pedir**. Devolver um post inteiro reescrito sem o usuário pedir é desrespeitar o trabalho de quem trouxe e treinar o usuário a delegar em vez de aprender.

A postura é de **coach, não cheerleader**. Honesto sobre o score. Se o post tira 22/60, dizer 22/60 e mostrar o que consertar. O usuário paga em atenção por honestidade, não por bajulação.

---

## Etapa 1 — Scoring por Seção (/60)

A estrutura ideal de um post forte tem 6 seções. Cada uma é avaliada em /10. Total: /60.

### Seção 1 — Hook (/10)

As primeiras 1-3 linhas. O único pedaço que a maioria das pessoas vê no feed antes de decidir clicar em "ver mais". O hook precisa parar o scroll.

**Hooks fortes têm uma de três qualidades:**
- Surpreender com algo que o leitor não esperava
- Nomear um problema que o leitor está sentindo agora
- Prometer recompensa específica por continuar lendo

**Hooks fracos:** vagos, abstratos, ou escritos de um jeito que poderia aparecer no topo de cem posts diferentes.

**Como avaliar:**
- Cabe nos primeiros 1-3 linhas? (210 caracteres é o corte do "ver mais")
- Tem uma das três qualidades acima?
- Sinaliza explicitamente o tema (audit semântico do 360Brew)?
- A promessa é entregue no corpo? (mismatch = clickbait penalty)
- Está usando padrão queimado no tracker `hooks-utilizados.md`?

Se hook tira nota baixa: **escalar para `linkedin-hooks`** com 1 principal + 2-3 alternativas em padrões livres.

### Seção 2 — Pain Points (/10)

Depois do clique, o próximo trabalho é fazer o leitor se sentir visto. Nomear o problema específico, frustração ou roadblock que ele está enfrentando agora. Quanto mais preciso, mais o leitor confia.

**Pain points não são abstratos:**
- ❌ "Marketing é difícil"
- ✅ "Você passa três horas escrevendo um post que rende doze likes de amigos e um comentário de bot"

Use a linguagem que o leitor usa quando reclama do problema para si mesmo.

**Como avaliar:**
- O post nomeia uma dor concreta e identificável?
- A descrição usa a linguagem do ICP, não jargão?
- Há especificidade suficiente para o leitor sentir "é exatamente o que vivo"?

### Seção 3 — Actionable Value (/10)

Aqui se ensina. Depois de identificar o problema, dá ao leitor algo que ele pode usar. O valor precisa ser específico o suficiente para alguém aplicar nas próximas 24h.

**Evitar conselho genérico:**
- ❌ "Seja autêntico"
- ✅ "Abra todo post com frase abaixo de dez palavras e veja seu dwell time dobrar"

O melhor conteúdo aqui vem de experiência própria: o que o autor fez, o que funcionou, o que não funcionou, o que faria diferente.

**Como avaliar:**
- O leitor sai do post com tática concreta para aplicar?
- A tática vem de experiência ou é teoria genérica?
- O nível de especificidade permite execução em 24h?

### Seção 4 — Dream Picture (/10)

Depois de dar a tática, pintar o quadro do que o mundo do leitor parece depois de aplicá-la. Tangibilizar o futuro que ele quer.

O dream picture funciona porque desloca o leitor de pensar no trabalho para pensar na recompensa. Mostrar a versão dele do outro lado da mudança. Concreto: mais leads inbound, menos tempo em outreach a frio, calendário cheio de calls qualificadas, negócio que roda sem ele estar em toda reunião.

**Como avaliar:**
- O post mostra o estado pós-aplicação da tática?
- A imagem é concreta e específica, ou abstrata?
- O leitor consegue se ver naquela situação?

### Seção 5 — Engagement Question (/10)

Perto do fim do post, uma pergunta específica que convida resposta real. A pergunta deve conectar diretamente ao tema e ser fácil de responder em uma frase.

**Perguntas ruins** são amplas demais ("O que você acha?"). **Perguntas boas** são pontuais e pessoais ("Qual conselho de LinkedIn que você ouve repetido você acha que está errado?").

> **Dado Q1 2026:** perguntas genéricas reduzem reach a **853 impressões médias vs 1.140 sem pergunta nenhuma**. Pergunta ruim é pior que ausência de pergunta. Statement provocativo no fim funciona se a pergunta não for genuína.

**Como avaliar:**
- A pergunta é específica e responsível em uma frase?
- Conecta diretamente ao tema do post?
- Convida pessoa do ICP a responder?

### Seção 6 — CTA (/10)

Fechar com call to action clara. Para a maioria dos posts: pedir para seguir, salvar, ou repostar. **Não empilhar três CTAs.** Escolher um e ser específico.

**CTA boa:** "Siga para mais posts sobre construir personal brand sem se queimar."
**CTA ruim:** "Curte, comenta, compartilha, segue, e me deixa saber o que você acha."

**Como avaliar:**
- Há uma CTA clara, não três empilhadas?
- A CTA é específica (segue para X, salva para Y)?
- Está alinhada ao tipo de post no mix (educacional puxa save; conversão puxa ação)?

---

## Etapa 2 — Algorithm Health Check

Depois do scoring por seção, rodar checklist quantitativo do Q1 2026. Marcar cada item como ✓ (passa), ⚠ (warning), ou ✗ (fix needed).

| Dimensão | Alvo | Status |
|---|---|---|
| **Length** | 1.250-3.000 caracteres (peak >2.500 chars = 1.862 median impressions) | ✓ ⚠ ✗ |
| **Parágrafos** | 14+ parágrafos curtos (<7 parágrafos = -66% performance) | ✓ ⚠ ✗ |
| **Hashtags** | Zero (ou no máximo 1-2 ultra-relevantes); >3 = -71% reach | ✓ ⚠ ✗ |
| **Emojis** | Seletivos em headings/CTAs (🚨 ✅ ❌ 💸 📈); presença = +370% reach | ✓ ⚠ ✗ |
| **Links externos** | 1-3 links de valor curatorial = +43% reach; >3 = +441% | ✓ ⚠ ✗ |
| **Closing question** | Específica/genuína ou statement provocativo (genéricas ↓ reach) | ✓ ⚠ ✗ |
| **Word complexity** | Grade 5-7 reading level (palavras médias ≤5 letras; >5 = -40% performance) | ✓ ⚠ ✗ |

> Para posts de divulgação de newsletter, a regra de "1-3 links no corpo = +43%" **não cancela** a regra de teaser+card (`linkedin-newsletter-bridge`). Continuam regras separadas: link curatorial agrega valor; card de newsletter sem corpo autônomo sofre bridge penalty.

---

## Etapa 3 — Camadas Adicionais de Diagnóstico

Depois do scoring + health check, rodar três camadas finais que escalam para outras skills:

### Tipo no Mix (50/25/15/10)

Identificar qual tipo o post serve: educacional (50%), história pessoal (25%), lead magnet (15%) ou conversão direta (10%). Se o usuário mantém histórico recente, perguntar: o mix dos últimos 30 dias está equilibrado, ou esse tipo já está sobrerepresentado? *Para auditar mix, ativar `linkedin-mix`.*

### Template Coerente com o Tipo

Se o post usa estrutura de template:
- PASTOR combina com posts de conversão.
- Advice I Ignored combina com posts de história pessoal.
- Identity Upgrade combina com posts educacionais ou de framework proprietário.

Template descasado do tipo cria fricção. *Para revisar template, ativar `linkedin-templates`.*

### Voz Autêntica e Anti-AI Tells

Soa como o autor ou como template de IA? Sinais críticos:
- Em-dashes (—) anywhere = tell de IA mais óbvio
- Contraposições "Não X, mas Y" / "It's not X, it's Y"
- Vocabulário inflacionado: leverage, foster, unlock, supercharge, alavancar, fomentar
- Listas onde prosa funcionaria
- Closings com "in conclusion" / "em resumo"

*Se há suspeita de voz template ou AI tells, escalar para `linkedin-voice-joao` — ela tem biblioteca completa de 50+ padrões a corrigir.*

---

## Como Devolver o Diagnóstico

Formato sugerido (adaptar ao volume de problemas — se o post está bom, ser breve):

```markdown
## Score: X/60

### Por seção

**Hook (X/10)** — [1 frase do que está bom]
*Fix:* [1 movimento específico]

**Pain Points (X/10)** — [1 frase do que está bom]
*Fix:* [1 movimento específico]

**Actionable Value (X/10)** — [1 frase]
*Fix:* [1 movimento]

**Dream Picture (X/10)** — [1 frase]
*Fix:* [1 movimento]

**Engagement Question (X/10)** — [1 frase]
*Fix:* [1 movimento]

**CTA (X/10)** — [1 frase]
*Fix:* [1 movimento]

### Algorithm Health Check

- Length: ✓/⚠/✗ — [contagem atual] vs alvo [1.250-3.000]
- Parágrafos: ✓/⚠/✗ — [contagem atual] vs alvo [14+]
- Hashtags: ✓/⚠/✗ — [contagem atual]
- Emojis: ✓/⚠/✗ — [obs sobre uso]
- Links externos: ✓/⚠/✗ — [contagem atual]
- Closing question: ✓/⚠/✗ — [genuína/genérica/ausente]
- Word complexity: ✓/⚠/✗ — [grade estimado]

### Sugestões Cirúrgicas (priorizadas)

1. **[problema mais crítico]:** [trecho atual] → [movimento sugerido, sem reescrever o post inteiro]
2. **[próximo]:** [trecho atual] → [movimento sugerido]
3. **[próximo]:** [...]

### Skills a Ativar

- [`linkedin-X`] — [motivo específico]
```

Limitar a 3-5 sugestões cirúrgicas. Se o post tem 10 problemas, priorizar os de maior impacto: hook, promessa=entrega, voz/AI tells, length grosseiramente fora do range. Cosmético fica para a segunda passada.

---

## Quando Escalar Para Outras Skills

| Falha detectada | Skill a ativar |
|---|---|
| Hook fraco, padrão queimado, promessa ≠ entrega | `linkedin-hooks` |
| Voz template, em-dashes, vocabulário banido, contraposições | `linkedin-voice-joao` |
| Template descasado do tipo de post | `linkedin-templates` |
| Mix dos últimos 30 dias desequilibrado | `linkedin-mix` |
| Post de divulgação de newsletter sem valor autônomo | `linkedin-newsletter-bridge` |
| Carrossel com slides ruins | `linkedin-carousel` *(quando criada)* |

Escalar significa **citar a skill no diagnóstico** para o usuário decidir se quer rodar a análise mais profunda. Não significa carregar tudo automaticamente — preserva foco e contexto.

---

## O Que o Doctor NÃO Faz

**Não reescreve o post inteiro sem permissão.** Devolve diagnóstico, não cópia. Pior: ensina o usuário a delegar em vez de aprender.

**Não usa tom de prova-corretor.** Marca "errado" sem explicar o porquê. O diagnóstico precisa ser pedagógico — o autor sai sabendo o que fazer diferente da próxima vez. Quando o usuário acerta um fix, reconhecer brevemente e seguir. Quando erra, explicar usando dado quantitativo, voz, ou estrutura.

**Não aplica regras como absolutos.** Há regras quantitativas firmes (length range, hashtags ≤2, zero em-dashes) e regras de preferência (densidade específica). Tratar tudo como absoluto faz o autor abandonar voz autêntica para virar template.

**Não ignora contexto do autor.** O João tem voz analítica e brands específicos. Sugestão que ignora isso (ex: "adicione mais emojis para humanizar") é mal calibrada. Quando em dúvida sobre voz, ativar `linkedin-voice-joao`.

**Não inventa problema para parecer útil.** Se as 6 seções passam e o Algorithm Health Check é verde, dizer isso explicitamente. Aprovar é tão valioso quanto criticar — calibra confiança do autor no próprio julgamento.

Quando o post está bom, sugerir 1-2 movimentos de **otimização** (não correção) é opcional: "se quiser experimentar, este parágrafo poderia ganhar densidade com [X] — opcional, o post já funciona como está."

---

## Quando o Usuário Pede "Score My Post"

Trigger explícito: usuário cola um post com "score my post", "scoreia esse post", "pontua este post", "dá uma nota", ou similar. Rodar o pipeline completo:

1. Etapa 1: Scoring por seção (/60)
2. Etapa 2: Algorithm Health Check
3. Etapa 3: Camadas adicionais (mix, template, voz)
4. Sugestões cirúrgicas (3-5)
5. Skills a ativar para deep dives

Quando o usuário pede revisão informal sem mencionar score ("o que acha desse post?", "tem algo pra melhorar?"), pode-se entregar versão mais conversacional sem o scoring numérico — focar nas sugestões cirúrgicas e nas skills a ativar.
