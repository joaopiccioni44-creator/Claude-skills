---
name: linkedin-voice-joao
description: >
  Filtro de calibração de voz autoral do João Piccioni para posts de LinkedIn.
  Use sempre que estiver criando, revisando ou adaptando texto de post — como
  filtro final antes de publicar. Também use quando o usuário pedir para "fazer
  soar mais como você", "evitar Claude genérico", "ajustar o tom", questionar
  se um texto soa autêntico, ou pedir para reescrever um trecho na voz dele.
  Esta skill codifica o fingerprint vocal do João: analítico, evita hipérbole,
  narrativa de practitioner-turned-builder (CIO institucional → AI-native
  builder), acumulação narrativa em vez de contraposição, dados específicos
  como âncora.
---

# Voz João — Filtro de Calibração Autoral

## Por que voz é skill separada

Voz é o que distingue um post do João de um post genérico sobre o mesmo tema. O 360Brew tem credibility scoring que detecta escrita template e penaliza distribuição. Mais importante: o leitor humano detecta voz inautêntica em segundos e não engaja.

Esta skill funciona como **filtro final** — depois do conteúdo estar definido, antes de publicar. Não cria post, não decide tema, não escolhe template. Recebe o texto e devolve calibração.

---

## Fingerprint Vocal — Os 6 Traços

### 1. Analítico, evita hipérbole

A voz do João desconfia de superlativos. Em vez de "revolucionário", "incrível", "game-changing", prefere descrição precisa do mecanismo: "comprime assimetria", "reduz fricção em [X]", "muda a função custo de [Y]". Se o adjetivo não muda a verdade da frase, ele sai.

**Antes:** "A IA é uma ferramenta absolutamente revolucionária que está transformando completamente o mercado financeiro."

**Depois:** "A IA está mudando o que conta como vantagem competitiva em mercado financeiro. O analista que lia PDF de relatório virou commodity em 2026."

### 2. Practitioner-turned-builder

Narrativa recorrente: 15 anos em asset management institucional (CIO de portfólio multi-asset) → fundador de Capital Pulse e construtor de PulseInvest.ai. Essa transição não é currículo — é argumento. Dá autoridade pra falar tanto da indústria tradicional quanto da AI-native, e cria curiosity gap natural ("como ele fez essa virada?").

Quando faz sentido invocar isso: posts de tese sobre AI no mercado, comentários sobre obsolescência de processos antigos, discussões sobre infra de gestão. Quando NÃO invocar: posts puramente educacionais sobre tema técnico, em que a credencial não acrescenta.

### 3. Acumulação narrativa em vez de contraposição

A voz do João constrói por **acréscimo**, não por oposição. Em vez de "Não é sobre X, é sobre Y", prefere "É sobre X. E também é sobre Y. E o que costura os dois é Z."

A estrutura "Não X, mas Y" está formalmente queimada — entra em conflito direto com a preferência narrativa dele e soa como template. Sempre reescrever em forma de acumulação ou em afirmação direta.

### 4. Tensão sem dramatismo

A voz do João sabe criar tensão sem usar dramatização. Em vez de "Isso vai destruir o mercado tradicional!", prefere "A janela está se fechando" ou "A vantagem competitiva está mudando de eixo". Tensão por implicação, não por exclamação.

Sinais de dramatismo a evitar: pontos de exclamação (raros, no máximo 1 por post se for inevitável), CAPS para ênfase, "URGENTE", "ATENÇÃO", "ÚLTIMO AVISO".

### 5. Dados específicos como âncora

Cada tese ganha credibilidade quando vem com número. Em vez de "muitos projetos open-source de finanças no GitHub", prefere "TradingAgents passou de 66 mil stars no GitHub". Em vez de "cresceu muito", prefere "compressão 10x desde 2022".

Quando o número não existe, citar a fonte que valida a afirmação ("conforme análise do Goldman Sachs", "no último relatório da CVM"). Voz analítica sustenta autoridade via evidência, não via assertividade.

### 6. Brands como infra, não como pitch

Capital Pulse, PulseInvest.ai e Exército de Agentes são mencionados como **infra que existe e está em uso**, nunca como produto sendo vendido. Frase típica do João: *"O Exército de Agentes que opera o Capital Pulse e o PulseInvest já é exatamente isso — pipeline heterogêneo, agentes especializados."*

A regra: se a frase poderia estar num pitch deck, reescrever. A frase certa descreve o que a infra faz no contexto da tese, não o que ela vende.

---

## Padrões Linguísticos a Evitar

| Padrão template | Por quê falha | Substituir por |
|---|---|---|
| "Não X, mas Y" | Queimado, soa template, conflita com preferência por acumulação | "É X. E também Y." ou afirmação direta |
| Estruturas paralelas exageradas ("X faz A. Y faz B. Z faz C.") | Cadência mecânica, identifica como AI | Variar comprimento de frase, quebrar paralelismo |
| "Em outras palavras" / "Ou seja" / "Em resumo" | Reformulação preguiçosa, denota IA explicando para si mesma | Cortar — se a frase anterior precisa de tradução, reescrever |
| Conclusão em forma de moral ("A lição é: ...") | Tom palestra, paternalista | Deixar a conclusão implícita; o leitor analítico tira a moral sozinho |
| Listas de adjetivos ("é poderoso, eficaz e escalável") | Esvazia significado, soa marketing | Escolher um adjetivo preciso ou substituir por mecanismo |
| "Imagine que..." / "Pense em..." | Recurso de palestrante motivacional | Aterrissar direto no exemplo |
| Reticências para suspense ("E o resultado foi...") | Suspense barato, infantiliza | Cortar e ir direto ao resultado |

---

## Movimentos Que Combinam Com a Voz

**Aterrissar em exemplo concreto cedo.** "Earnings transcript + sentimento Glassdoor + atividade LinkedIn da liderança + fato relevante CVM + busca de patentes." Lista específica, sem explicação prévia. O leitor monta o panorama sozinho.

**Citar referências canônicas do nicho.** Renaissance Technologies, Long-Term Capital, Stratechery, Patrick O'Shaughnessy. Ativa associação imediata em quem é do nicho e cria curiosity gap em quem não é.

**Usar timestamps quando há transformação real.** "Em 2022 isso era PowerPoint. Hoje é stack open-source executável." Dois pontos no tempo + objeto da mudança = curiosity gap automático.

**Fazer a virada interpretativa logo após o dado.** "Taxa de default subiu 23%. O mercado não precificou." Dado + leitura = autoridade analítica. Dado solto = manchete.

**CTA que nomeia setor específico.** "Para quem está em mesa de gestão tradicional no Brasil hoje:" — em vez de "Você pensa diferente?". Qualifica o cluster que o algoritmo aprende sobre o autor.

**Usar "blablabla" como recurso satírico seletivo.** Marca registrada do João para sinalizar discurso vazio de C-levels ou mercado. Usar com parcimônia — se virar tique, perde efeito.

---

## Como Aplicar a Skill como Filtro

Quando ativada sobre um texto:

1. **Ler o texto inteiro** sem editar — entender a intenção primeiro.
2. **Marcar trechos suspeitos** de voz template (padrões da tabela acima).
3. **Verificar densidade analítica** — há dados, mecanismos, exemplos concretos?
4. **Verificar dramatismo** — pontos de exclamação, CAPS, superlativos?
5. **Verificar como brands aparecem** (se aparecem) — infra ou pitch?
6. **Devolver feedback em 3 níveis:**
   - **Trechos a cortar** — frases template que somem
   - **Trechos a reescrever** — propor versão calibrada
   - **Trechos que estão na voz** — apontar (positive reinforcement, ajuda o autor a calibrar instinto)

Não reescrever o post inteiro. Cirurgia, não transplante.

---

## Exemplos de Voz do João (referência)

Posts publicados recentemente que exemplificam a voz calibrada vivem em `/Users/joaopiccioni/Documents/Claude/Projects/LinkedIn & Instagram/`. Em particular:

- `2026-05-08-post-ai-hedge-fund.md` — Profecia/analogia histórica (Renaissance), dados ancorados (66k stars, 10x inference), brands como infra ("Exército de Agentes que opera o Capital Pulse"), CTA com setor nomeado ("mesa de gestão tradicional no Brasil")
- `2026-05-03-post-linkedin-ai-displacement-paradox-solis.md` — voz analítica em tema de transformação tecnológica

Ler esses arquivos quando precisar calibrar voz num tema parecido. São referência viva, não template — a voz evolui, mas o fingerprint persiste.

---

## Quando NÃO Aplicar Esta Skill

- Em posts de outras pessoas (ela é específica para João)
- Em conteúdo que pede tom diferente por design (ex: post leve para Instagram que não pede a voz analítica do LinkedIn)
- Quando o usuário pediu explicitamente para experimentar voz diferente (ex: "quero testar tom mais informal nesse post")

Se houver dúvida se a skill se aplica, perguntar antes de filtrar.
