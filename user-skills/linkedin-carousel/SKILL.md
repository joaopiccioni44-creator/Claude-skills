---
name: linkedin-carousel
description: >
  Constrói carrosseis (PDF multi-slide) para LinkedIn alinhados ao algoritmo
  360Brew e ao Q1 2026 report — formato com maior viralidade da plataforma
  (29% dos top 1% posts, ~3x reach vs text post). Use sempre que o usuário
  pedir carrossel, slide deck para LinkedIn, infográfico multi-slide, framework
  visual, mencionar "vou fazer um carrossel sobre X", "8 slides", "10 slides",
  ou quiser estrutura visual para tese, framework, análise ou checklist. Esta
  skill cobre arquitetura de slides + briefing visual; integra explicitamente
  com infographic-prompt (geração do briefing para Nano Banana / Ideogram) e
  canvas-design (renderização final em PDF). Para o copy de cada slide, ativa
  linkedin-voice-joao como filtro final.
---

# LinkedIn Carousel — Estrutura e Workflow

## Por que carrossel é o formato mais valioso de 2026

Dados do Q1 2026 (397.605 posts analisados):

- **Carrosseis e infographics = ~3.0x reach** vs text post
- **Infographics dominam o top 1%:** 29% de todos os posts no top 1% são infographics
- **Engagement médio 6.6%** (vs 1-2% de text post)
- **AI-generated infographics em ascensão:** posts dessa categoria gerando 218k, 162k, 148k views recentes
- **Portrait orientation +47% vs landscape:** alvo é 1200x1500px (ratio 4:5)
- Cada swipe é registrado como sinal de engajamento + dwell time pelo 360Brew — múltiplos swipes em sequência = sinal forte de qualidade

A combinação de viralidade alta + dwell time longo + saves repetidos faz do carrossel o melhor formato para conteúdo educacional e frameworks proprietários — exatamente o tipo que constrói credibility cluster.

---

## Estrutura Padrão: 8-10 Slides

O sweet spot é **8-10 slides**. Range geral aceitável: 8-12. Acima de 12 perde leitura completa; abaixo de 7 não maximiza dwell time.

### Slide 1 — Hook Visual (cover)

A capa é o equivalente do hook do post. Stop-scroll absoluto.

- **Hook textual** (até 6 palavras, formato grande): tira do mesmo padrão que o `linkedin-hooks` recomenda — Tensão de Identidade, Contrarian, Profecia, Promessa de Framework. Adaptado para impacto visual.
- **Imagem ou ícone de fundo** que reforça a tensão (sem texto pequeno na cover; tudo precisa ser legível em thumbnail mobile).
- **Indicador "swipe" sutil** (seta, número 1/N, ou call para a página seguinte).

Exemplo de hooks de cover validados pelo João:
- *"A próxima Renaissance Tech vai ter 5 pessoas e 2 MacBooks"* — Profecia/analogia histórica
- *"O analista que ainda lê PDF virou commodity"* — Tensão de Identidade
- *"6 fontes que separam alpha de ruído em 2026"* — Promessa de Framework numerada

### Slide 2 — Statement Contrarian / Hook Reforçado

O slide 2 é onde o leitor decide se continua. Aqui vai a **afirmação mais forte do carrossel**, normalmente a tese central que vai ser desenvolvida nos slides seguintes.

Padrão: uma frase só, fonte grande, alto contraste visual. Sem dado, sem nuance — só a afirmação que pega.

### Slides 3 a (N-1) — Desenvolvimento Lógico

Aqui vai o conteúdo. A regra de progressão é **tensão → resolução**:

- Slides 3-4: aprofundar o problema, mostrar custo de ignorar
- Slides 5-7: entregar a solução em partes (passos, fontes, princípios — depende do formato)
- Slide N-1: implicação prática ou síntese

**Densidade por slide:** uma ideia por slide. No máximo 3 bullets curtos OU um framework visual OU um chart com 1-2 linhas de leitura. Slide com texto corrido perde — leitor não rola para ler parágrafo num carrossel.

### Slide N (último) — CTA ou Pergunta

Encerra com **uma única ação clara** (não empilhar três CTAs). Opções:

- **CTA explícito**: "Salva esse carrossel — vai usar nas próximas reuniões de alocação."
- **Pergunta específica**: "Qual dessas 6 fontes você já incorporou no seu pipeline?"
- **Statement provocativo**: "Quem chegar em 2027 sem esse stack vai competir com gestoras tier-1 rodando o mesmo."
- **Convite ao próximo passo**: "Comente 'STACK' e mando o link da newsletter Capital Pulse com o setup completo."

> Lembrar: carrossel é o formato com maior potencial de **save**, e save vale 5-10x mais que like no 360Brew. CTA "salva esse post" geralmente paga mais que pedir comentário.

---

## Tipos de Carrossel para o João

Mapeamento dos formatos recorrentes que casam com os pilares dele:

### Framework Explainer

Apresenta um framework próprio do João (Exército de Agentes, Pipeline de 6 Fontes, etc.) em formato visual de passos numerados.

- Slide 1: nome do framework + promessa (Promessa de Framework)
- Slide 2: tese central (por que esse framework existe)
- Slides 3-(N-1): cada slide = uma etapa do framework, com ícone + 1 frase explicativa + exemplo concreto
- Slide N: CTA para salvar/aplicar

### Análise de Mercado

Tese de mercado com dados ancorados (estilo do post `2026-05-08-post-ai-hedge-fund.md`).

- Slide 1: hook contrarian ou de profecia
- Slide 2: dado específico que ancora a tese
- Slides 3-5: 3-4 evidências numeradas (cada uma com fonte/número)
- Slides 6-7: leitura/implicação prática
- Slide N: CTC com setor nomeado

### Dispatches de Evento (modelo SXSW)

Cobertura de evento ao vivo ou síntese pós-evento.

- Slide 1: contexto do evento + ângulo único
- Slides 2-(N-1): insights numerados ou painéis específicos com aprendizado
- Slide N: síntese + convite para próxima parte da série

### Checklist Educacional

Formato save-worthy puro, alta probabilidade de captura para lista própria.

- Slide 1: promessa de framework numerada
- Slides 2-(N-1): cada slide = item da checklist com 1 frase explicativa
- Slide N: CTA para salvar + opcional lead magnet

---

## Integração Com Outras Skills

Carrossel é trabalho multi-skill. Pipeline natural:

| Etapa | Skill ativa |
|---|---|
| Decidir tipo de carrossel | Esta skill (mapeamento acima) + `linkedin-mix` se houver dúvida sobre tipo no funil |
| Escrever copy de cada slide (texto curto, denso) | Esta skill + `linkedin-voice-joao` como filtro final em cada slide |
| Hook do slide 1 (cover) | `linkedin-hooks` (consulta tracker, escolhe padrão livre) |
| Framework persuasivo se for educacional | `linkedin-templates` (Identity Upgrade encaixa bem em Framework Explainer) |
| Briefing visual para gerador de imagem | `infographic-prompt` (skill global do João, gera prompt para Nano Banana / Ideogram) |
| Renderização final em PDF | `canvas-design` (skill global, ou export direto do Paper.design via `epic-paper`) |
| Diagnóstico antes de publicar | `linkedin-post-doctor` (avalia o post de texto que acompanha o carrossel) |

---

## Texto que Acompanha o Carrossel (post body)

Carrossel publicado no LinkedIn vem com um post de texto. Esse texto também passa pelas regras gerais (length 1.250-3.000 chars, 14+ parágrafos, etc.).

**Padrão eficaz:**

```
[Hook que repete ou expande a tensão da cover do carrossel]

[Contexto: por que esse carrossel existe / o que ele resolve / quando você
percebeu que precisava sistematizar isso]

[1-2 parágrafos de tese própria — a opinião do João sobre o tema do
carrossel, que NÃO está nos slides]

[CTA específico: "Os 8 slides estão abaixo." / "Salva o carrossel e me diz
qual etapa você está começando agora."]
```

O texto **não pode duplicar** o conteúdo do carrossel. Ele complementa: dá contexto, traz opinião pessoal, ancora autoridade. O carrossel entrega a estrutura; o texto entrega o ponto de vista.

---

## Workflow Completo

1. **Definir tipo** de carrossel (Framework Explainer / Análise de Mercado / Dispatches / Checklist).
2. **Escrever a estrutura** em outline: o que cada slide carrega (1 linha por slide).
3. **Validar densidade**: cada slide tem uma ideia única e legível em 3 segundos?
4. **Escrever o copy** de cada slide. Curto, denso, sem fillers (`linkedin-voice-joao` pra filtrar).
5. **Definir o hook da cover** com `linkedin-hooks` (consulta tracker de hooks queimados).
6. **Briefar o visual** com `infographic-prompt` — gera prompt detalhado para Nano Banana / Ideogram, ou prepara para `canvas-design` / `epic-paper`.
7. **Renderizar** os slides em PDF (ratio 4:5, 1200x1500px, info no centro porque bordas podem cropar).
8. **Escrever o post de texto** que acompanha (regras gerais de 360Brew + `linkedin-voice-joao`).
9. **Diagnóstico** com `linkedin-post-doctor` se quiser scoring /60.
10. **Publicar e responder comentários** nos primeiros 60 minutos (engagement velocity).

---

## Notas de Implementação

**Mobile-first sempre.** 72% do uso do LinkedIn é mobile. Validar todo slide num preview de 375px de largura antes de finalizar — texto que fica bom no desktop pode virar borrão no celular.

**Bordas perdidas no crop.** O LinkedIn corta as bordas em algumas previews; informação crítica vai no centro do slide.

**Cores e fonts consistentes.** Carrossel é vitrine de marca visual. Manter paleta + 1-2 fontes consistentes ao longo do carrossel (e idealmente entre carrosseis do mesmo autor). Conexão com `theme-factory` se quiser sistematizar.

**Não force frequência.** Carrossel custa tempo (texto + visual + renderização). Melhor 1 carrossel forte por mês do que 4 medíocres. O Q1 2026 confirma: 1-2 posts excelentes/semana superam posting diário com qualidade média.

**Reaproveitar inteligente.** Um carrossel forte vira newsletter expandida em Capital Pulse, vira post Instagram (mesmo design adaptado para 1080x1080 ou 1080x1350), vira thread no X. *Para profundidade nessa adaptação, ativar `linkedin-repurposing` (quando criada).*

**AI-generated dominando.** Não há mais penalidade por usar IA para gerar a parte visual — os exemplos do report mostram AI-generated infographics no topo. O critério é qualidade do briefing (e por isso `infographic-prompt` é skill load-bearing).
