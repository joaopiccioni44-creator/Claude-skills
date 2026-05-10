---
name: linkedin-newsletter-bridge
description: >
  Constrói posts no LinkedIn que divulgam newsletter (Capital Pulse, Substack,
  Beehiiv, LinkedIn Newsletter) ou artigo externo SEM sofrer bridge penalty do
  algoritmo 360Brew. Use sempre que o usuário pedir post para divulgar
  newsletter, "post do Capital Pulse", "vou divulgar a newsletter desta
  semana", "post com card de link", ou mencionar bridge penalty, teaser,
  off-platform behavior. Codifica a regra empírica do Q1 2026: posts no formato
  "teaser + card" sofrem 16x menos alcance vs posts de thought leadership do
  mesmo criador. A regra do report sobre links no corpo (1-3 = +43% reach,
  >3 = +441%) NÃO cancela essa restrição — ela vale para links curatoriais que
  agregam ao argumento, não para card de promo de newsletter sem corpo autônomo.
---

# LinkedIn Newsletter Bridge — Como Divulgar Sem Matar o Alcance

## A regra empírica que move tudo

Posts que promovem newsletter ou artigo externo sofrem **bridge penalty** quando formatados como "teaser + card de link". O algoritmo 360Brew lê o card de link como intenção de tráfego de saída e freia a distribuição **antes mesmo de medir engajamento**.

Dado validado empiricamente em comparativo do mesmo criador, mesma semana:

- Hook com tensão de identidade + imagem: **3.628 impressões, 2.469 usuários**
- Hook informativo sem tensão: **256 impressões, 162 usuários**
- **Newsletter como teaser + card: 223 impressões, 140 usuários** ← o pior performer

**Diferença: 16x menos alcance** que posts de thought leadership do mesmo criador.

A causa não é o card em si — é a ausência de valor autônomo no corpo. Quando o post não entrega nada para quem não clica, o dwell time despenca e o algoritmo freia.

---

## Distinção Crítica: Card de Newsletter vs. Link Curatorial

O Q1 2026 report trouxe um dado que **parece contradizer** a regra acima: posts com 1-3 links externos têm **+43% reach** e posts com >3 links têm **+441% reach**. Como conciliar?

A reconciliação é simples e load-bearing para esta skill:

| Tipo | Comportamento do algoritmo | Regra |
|---|---|---|
| **Link curatorial agregando ao argumento** (referência, fonte, recurso citado) | +43% / +441% reach | Inclua livremente quando o link reforça a tese |
| **Card de newsletter como promo principal** (teaser do conteúdo da newsletter) | Bridge penalty (-16x reach) | Reescreva como post autônomo + card como bônus |

A diferença é **quem é a estrela**. Se o post existe para chamar o leitor para fora da plataforma, é bridge. Se o link existe para fortalecer um argumento que já está sendo feito autonomamente no post, é curatorial.

---

## O Formato Correto

A regra prática é uma só: **escreva o post como se o card não existisse**. Se o post não funciona de forma autônoma, reescreva antes de publicar.

```
[HOOK com tensão de identidade, distinção analítica, profecia ou outro
 padrão livre no tracker — ativar linkedin-hooks]

[ARGUMENTO COMPLETO no corpo — 1.250-3.000 caracteres, 14+ parágrafos.
 O post precisa ser valioso para quem nunca vai clicar na newsletter.
 Trate o leitor que não clica como o leitor mais importante: o algoritmo
 mede o dwell time dele, não a conversão para fora.]

[CTC reflexivo que convida comentários de setores específicos — não
 "compartilha sua opinião nos comentários", e sim "qual setor você está
 vendo essa dinâmica primeiro?" ou similar com nome de público]

[Card da newsletter — apresentado como BÔNUS para quem quer aprofundar,
 não como destino do post. Linguagem típica: "Para quem quer o
 desdobramento completo dessa tese com os 6 dados que sustentam,
 expandi tudo na edição desta semana do Capital Pulse: [link]"]
```

O leitor que não clica deve ter consumido valor real. Esse consumo é o que o algoritmo mede.

---

## Antes vs. Depois — Exemplos

### Cenário: divulgar edição do Capital Pulse sobre "AI no asset management"

**Formato errado (teaser + card):**

```
Acabou de sair a nova edição do Capital Pulse.

Tema: como a IA está mudando o asset management.

Você vai descobrir as 5 mudanças que estão acontecendo agora.

Link nos comentários ↓

[CARD DA NEWSLETTER]
```

Por que falha: zero valor autônomo. O leitor sai da leitura sabendo apenas que existe uma newsletter sobre o tema. Dwell time despenca, bridge penalty é máxima.

**Formato correto (post autônomo + card como bônus):**

```
[HOOK] O analista que ainda lê PDF de relatório virou commodity em 2026.

[CONTEXTO] Não é hipérbole. É a leitura direta do que aconteceu nos últimos
18 meses no asset management institucional brasileiro, e que a maioria dos
incumbentes ainda não precificou.

[ARGUMENTO COMPLETO — 5-7 parágrafos com a tese sustentada por dados
específicos, sem precisar do link para entender]

[CTC] Para quem está em mesa de gestão tradicional no Brasil hoje: qual
o seu pipeline de captura de sinal não-estruturado? Se a resposta envolve
analista lendo PDF de relatório, a janela está fechando.

[BÔNUS — opcional, ao final, sem destaque visual] Desdobrei essa tese com
os 12 dados de mercado que sustentam ela na edição desta semana do
Capital Pulse: [link]

[CARD]
```

Por que funciona: o leitor que não clica recebeu uma tese completa, ancorada em dados, com CTA reflexivo. Dwell time alto, save-rate alto, comentário substantivo. O card vira **upgrade**, não chamada de saída.

---

## Checklist de Validação Pré-Publicação

Antes de publicar qualquer post que divulga newsletter ou artigo externo, rodar estas perguntas:

- [ ] Se eu remover o card e o link, o post ainda entrega valor completo?
- [ ] O corpo tem 1.250-3.000 caracteres com argumento sustentado?
- [ ] O hook está em padrão livre no tracker (`hooks-utilizados.md`)?
- [ ] O hook NÃO é "Acabou de sair / Nova edição / Confira"?
- [ ] Há ao menos 2 dados específicos no corpo (números, fontes, exemplos)?
- [ ] O CTC nomeia setor ou grupo específico?
- [ ] O card aparece DEPOIS da CTC, posicionado como bônus, não como destino?
- [ ] O texto de transição para o card é "expandi/desdobrei isso em [link]" e não "leia mais em [link]"?

Se qualquer uma das respostas é "não", reescrever antes de publicar.

---

## Casos de Uso Específicos

### Capital Pulse (newsletter principal do João)

Capital Pulse roda regularmente. Cada edição vira potencial post no LinkedIn. O ângulo do post NÃO é "saiu nova edição" — é uma tese própria sobre o tema da edição, com a edição posicionada como aprofundamento opcional.

**Cadência recomendada:** 1 post por edição, no mesmo dia ou no dia seguinte ao envio. Não fazer 2 posts diferentes promovendo a mesma edição (cansa audiência e cria sinal de spam para o algoritmo).

### Posts com link para artigo no Substack / Beehiiv

Mesmas regras. O link no corpo (curatorial, ao fim) tem benefício do +43% reach se o post é autônomo. Se o post existe só para mandar tráfego pro Substack, vira bridge.

### Posts com link para PulseInvest.ai

Não é newsletter, mas é externo. Mesmas regras. PulseInvest aparece como "infra que existe" na voz do João (`linkedin-voice-joao`), nunca como pitch. O post precisa entregar valor autônomo sobre o tema (portfólios AI, métricas comparativas, etc.) e o link é referência para quem quer ver os dados ao vivo.

### Posts com link para vídeo no YouTube ou outro

Mesmas regras. Importante: o LinkedIn penaliza link de YouTube em particular (mais que outros). Se o vídeo tem upload nativo possível, fazer upload nativo + mencionar que tem versão estendida no YouTube no fim.

---

## Conexão Com Outras Skills

| Job | Skill ativa |
|---|---|
| Hook do post de divulgação | `linkedin-hooks` (consulta tracker, hooks como "Acabou de sair" estão queimados implicitamente) |
| Calibração de voz no corpo | `linkedin-voice-joao` (filtro final + anti-AI tells) |
| Estrutura de 6 seções para o corpo autônomo | `linkedin-360brew` (estrutura) ou `linkedin-templates` (PASTOR ou Identity Upgrade) |
| Diagnóstico antes de publicar | `linkedin-post-doctor` (scoring /60) |
| Construção do funil de email atrás da newsletter | `linkedin-deplatforming` (quando criada) |

---

## Notas de Implementação

**Bridge penalty é cumulativa.** Postar várias divulgações de newsletter em sequência sinaliza ao algoritmo que o autor é distribuidor, não criador. Intercalar com posts puramente analíticos (sem link externo) preserva a percepção de criador nativo.

**Comentários no primeiro comentário não substituem corpo autônomo.** O truque velho de "link nos comentários ↓" não resolve bridge penalty se o corpo continua sendo teaser. O algoritmo lê o post inteiro, não só o link.

**Evite linguagem promocional.** "Não perca", "imperdível", "exclusivo", "última chance", "garante já". Sinaliza marketing, dispara filtros de qualidade. O post precisa soar como pensamento próprio que casualmente menciona um aprofundamento disponível.

**Post de divulgação ainda conta no mix.** No 50/25/15/10 (`linkedin-mix`), post de newsletter geralmente cai como educacional (50%) ou conversão (10%, se a newsletter é gateway de funil pago). Manter dentro do orçamento do mix mensal.
