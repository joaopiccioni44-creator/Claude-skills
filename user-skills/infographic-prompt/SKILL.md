---
name: infographic-prompt
description: Gera prompts de alta qualidade para infográficos visuais prontos para uso em geradores de imagem como Nano Banana Pro, Nano Banana 2 e Ideogram. Use esta skill sempre que o usuário quiser criar um infográfico, visualizar um framework, transformar uma seção de texto em visual, criar thumbnail de newsletter ou post, ou montar um prompt para qualquer gerador de imagem com foco em design informacional. Acione também quando o usuário mencionar "infográfico", "prompt para imagem", "visualizar o framework", "thumbnail", "banner" ou pedir para "montar um prompt".
---

# Infographic Prompt Generator

Skill para construir prompts precisos e sistemáticos que geram infográficos de alta qualidade — do mesmo nível de um infográfico editorial profissional com hierarquia visual clara, paleta coesa, ícones expressivos e estrutura informacional densa.

## Referência de qualidade

O infográfico ideal tem estas características visuais:
- **Hierarquia tipográfica**: título bold + subtítulo leve + headers de seção + body text — 4 níveis distintos
- **Paleta coesa**: cor primária dominante (azul/roxo), acento vibrante (laranja/âmbar), fundo neutro, texto escuro
- **Ícones semi-3D com gradiente**: não flat puro, não 3D pesado — o ponto médio que dá profundidade sem perder leitura
- **Elementos de dados**: tabelas de comparação, gráficos de curva, pirâmides de camadas, diagramas de Venn
- **Densidade equilibrada**: informação rica, mas cada bloco com espaço de respiro
- **Composição em grid**: painéis com fronteiras implícitas, não explícitas

---

## Passo 1 — Entender o conteúdo

Antes de montar o prompt, extrair do texto/contexto fornecido:

1. **Mensagem central**: O que o infográfico precisa comunicar em uma frase?
2. **Tipo de estrutura lógica** (escolher um):
   - Hierarquia / camadas (ex: framework de 4 estados)
   - Comparação binária (ex: replicável vs. não-replicável)
   - Progressão / linha do tempo (ex: curva de compounding)
   - Causa e efeito (ex: ação → consequência)
   - Tensão / pergunta em aberto (ex: quem fica com o ativo?)
   - Processo / fluxo (ex: onboarding → acúmulo → resultado)
3. **Quantos conceitos principais?** (2 a 6 elementos visuais distintos)
4. **Tem dado visual?** (tabela, gráfico, número destacado, percentual)

---

## Passo 2 — Selecionar o layout

Com base na estrutura lógica identificada:

| Estrutura | Layout ideal |
|-----------|-------------|
| Hierarquia / camadas | Stack vertical ou pirâmide |
| Comparação binária | Split horizontal (2 colunas) |
| Progressão / curva | Gráfico com anotações + texto lateral |
| 4+ conceitos paralelos | Grid 2×2 ou 4 colunas horizontais |
| Tensão / pergunta | Composição central com dois pólos e elemento de tensão no meio |
| Processo / fluxo | Sequência horizontal com setas ou conectores |
| Framework misto | Dois painéis: anatomia (esq.) + dinâmica (dir.) |

---

## Passo 3 — Definir a paleta

Escolher um dos esquemas validados:

**Paleta Executiva** (padrão para newsletters e LinkedIn):
- Fundo: branco ou navy escuro (#0A0F2C)
- Primária: roxo/azul (#6B4EFF ou #3B82F6)
- Acento: âmbar ou laranja (#F59E0B ou #FF6B35)
- Texto: navy escuro ou branco

**Paleta Editorial Escura** (alto contraste, impacto visual):
- Fundo: navy profundo (#0A0F2C)
- Primária: azul elétrico (#38BDF8)
- Acento: âmbar (#F59E0B)
- Brilho nos elementos principais: glow suave

**Paleta Clean Minimalista** (mais leve, institucional):
- Fundo: cinza muito claro (#F8FAFC)
- Primária: azul médio (#2563EB)
- Acento: verde ou laranja
- Texto: cinza escuro

---

## Passo 4 — Selecionar ícones e elementos visuais

Para cada conceito, indicar no prompt o ícone mais evocativo:

- Raciocínio / mente: `brain icon`, `neural network`, `thought nodes`
- Bloqueio / exclusividade: `padlock icon`, `shield icon`
- Crescimento / compounding: `exponential curve`, `upward arrow`
- Transferência / saída: `walking figure`, `door`, `arrow leaving`
- Dados / análise: `chart`, `table`, `magnifying glass`
- Conexão / rede: `nodes and edges`, `interconnected dots`
- Tempo / acúmulo: `hourglass`, `calendar layers`, `stacked rings`
- Empresa / organização: `building icon`, `org chart`

---

## Passo 5 — Montar o prompt por modelo-alvo

### Nano Banana 2 (Genspark)
- **Comprimento**: curto e direto (4–7 linhas)
- **Estrutura**: sujeito → cena visual → estilo → paleta
- **Não usar**: descrições longas, listas internas, vírgulas em excesso
- **Formato**:
```
[Descrição da cena/layout em 1-2 frases].
[Elementos visuais principais com ícones].
[Estilo]: flat cartoon illustration / clean infographic illustration.
[Paleta]: [cores]. No text. [Ratio].
```

### Nano Banana Pro (Genspark)
- **Comprimento**: médio (8–14 linhas)
- **Estrutura**: pode ser mais descritivo na disposição dos elementos e hierarquia
- **Ponto forte**: renderização de estrutura, coerência de layout, tabelas
- **Formato**:
```
[Tipo de infográfico e layout]. [Dimensão/ratio].
[Descrição detalhada de cada painel ou seção].
[Ícones e elementos visuais por área].
[Hierarquia visual: o que é maior, o que brilha, o que é distinto].
[Estilo]: clean editorial infographic illustration, [outros qualificadores].
[Paleta]: [cores detalhadas]. No decorative elements. No watermark.
```

### Ideogram
- **Comprimento**: mais longo e fluido (10–18 linhas)
- **Ponto forte**: renderização de texto em imagem, paleta, composição editorial
- **Pode incluir**: labels de texto dentro da imagem com mais confiança
- **Formato**:
```
[Tipo de infográfico]. [Layout e ratio].
[Cena e hierarquia visual em prosa descritiva].
[Cada seção com seu conteúdo, ícone e posição].
[Relação visual entre elementos — o que contrasta, o que conecta].
[Estilo]: [qualificadores de estilo editorial].
[Paleta]: [cores específicas com qualificadores de luminosidade].
No text (ou: with readable labels in [idioma]).
No watermark.
```

---

## Passo 6 — Instruções para texto dentro da imagem

Se o modelo-alvo lida bem com texto (Ideogram tem melhor renderização):
- Usar labels curtos (1–3 palavras por elemento)
- Evitar frases completas dentro da imagem — o corpo do texto fica na legenda/newsletter
- Se o texto sair distorcido: gerar sem texto e adicionar no Canva

Se o modelo-alvo tem renderização de texto instável (NB2):
- Descrever os elementos visuais sem labels dentro da imagem
- Indicar `no text` explicitamente no prompt
- Sugerir ao usuário adicionar texto em pós-edição (Canva, Figma)

---

## Exemplos de prompts prontos

### Framework de 4 camadas — Nano Banana Pro (horizontal)
```
Infographic illustration, horizontal layout, 16:9.
Four columns side by side. First three columns: equal-sized flat blocks
in muted navy blue, each with a small padlock icon at the top and labels
"Behavioral State", "Memory State", "Organizational Context State".
A subtle tag beneath each reads "replicable".
Fourth column: visibly larger, glowing electric blue, radiating soft
light outward, brain-circuit icon at top, label "Human-AI State",
tag beneath reads "irreplaceable".
Clean separation between columns. Dark navy background, electric blue
and amber accents, bold outlines, flat editorial illustration style,
modern and minimal. No decorative elements. 16:9 ratio.
```

### Tensão / pergunta em aberto — Nano Banana Pro (horizontal)
```
Infographic illustration, horizontal composition, 16:9.
Left side: a professional walking through an open door, carrying a
briefcase, glowing electric blue aura around them.
Right side: a minimalist office desk with a laptop, also emitting a
faint glowing aura.
Between them, the glowing aura stretches like a taut luminous thread
connecting both sides, visibly under tension. At the center of the
thread, a large bold question mark glowing in amber.
Below the scene, three small equal blocks labeled "Labor Law",
"Intellectual Property", "Platform Terms" — each with a distinct
muted color, slightly overlapping.
Dark navy background, electric blue and amber accents, flat editorial
cartoon style, bold outlines, clean minimal design. No watermark.
```

### Curva de compounding — Ideogram (horizontal)
```
Editorial infographic illustration, horizontal layout, 16:9.
Right side: a clean exponential curve graph. X-axis labeled "Time".
Y-axis labeled "Productivity". Two diverging curves: upper curve in
electric blue (labeled "Veterans"), lower curve in muted orange
(labeled "New Hires"). An inflection marker at the 9-12 month point
on the x-axis. Above the graph, a bold text annotation: "Inflection
Point: 9 to 12 months". Right of the graph, two short text blocks:
"Retention as Asset Protection" and "The 2028 Gap".
Left side: a small walking professional figure with a glowing neural
aura, surrounded by interconnected thought nodes.
White background, navy blue and electric blue primary colors, amber
accent, clean sans-serif labels, modern editorial infographic style.
No watermark.
```

---

## Output esperado da skill

Ao final do processo, entregar:

1. **Prompt principal** — para o modelo-alvo solicitado, pronto para colar
2. **Prompt alternativo** — variação de layout ou composição (quando relevante)
3. **Nota de pós-edição** — se há risco de texto distorcido, sugerir elementos a adicionar no Canva

Não entregar análise extensa. Ir direto ao prompt.
