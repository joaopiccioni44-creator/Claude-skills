---
name: linkedin-hooks
description: >
  Cria, propõe, revisa e diagnostica hooks (primeiros 210 caracteres) para posts
  do LinkedIn alinhados ao algoritmo 360Brew. Use sempre que o usuário pedir
  hook, gancho, abertura, primeira linha, ou quiser melhorar o início de um post.
  Também use quando mencionar Tensão de Identidade, Distinção Analítica,
  Contrarian, Profecia histórica, Timestamp Transformation, FOMO Insider, ou
  qualquer padrão de hook. ANTES de propor qualquer hook, esta skill OBRIGATORIAMENTE
  consulta o tracker hooks-utilizados.md no projeto LinkedIn & Instagram para
  evitar repetição de padrões queimados. Após aprovação do hook, atualiza o tracker.
---

# LinkedIn Hooks — Skill Operacional

## Por que o hook é decisivo

O hook são os primeiros 210 caracteres antes do "Ver mais" expandir o post. O 360Brew aplica **3-5x mais atenção** ao início (fenômeno *Lost in Distance*: o modelo prioriza semanticamente o que vem primeiro). Hook bom não significa engajamento — significa que o post entra na distribuição de verdade. Hook fraco mata o post antes mesmo de ter chance.

Análise comparativa de posts reais mostrou diferença de **14x no alcance** entre hooks com e sem tensão de identidade no mesmo criador, na mesma semana. O delta é gigante e justifica tratar hook como artefato dedicado.

---

## As 3 Qualidades de um Hook Forte

Independente do padrão escolhido, todo hook forte tem ao menos uma destas três qualidades. Hooks que não têm nenhuma das três falham invariavelmente.

**1. Surpreender com algo que o leitor não esperava.** O cérebro engaja com violação de expectativa. "A próxima Renaissance Technologies vai começar com cinco pessoas, dois MacBooks e GitHub aberto" surpreende porque desafia a imagem mental que o leitor tinha sobre como hedge funds nascem.

**2. Nomear um problema que o leitor está sentindo agora.** Identificação instantânea. "O analista que ainda lê PDF de relatório virou commodity em 2026" nomeia uma ansiedade que muitos analistas tradicionais sentem mas não verbalizam.

**3. Prometer recompensa específica por continuar lendo.** Curiosity gap honesto. "O framework que uso para avaliar risco de crédito em 3 etapas:" promete entrega concreta. A promessa precisa ser cumprida no corpo, ou vira clickbait penalty.

**Hook fraco** é aquele que poderia aparecer no topo de cem posts diferentes escritos por cem pessoas diferentes. Se o hook não passa o teste "isso poderia ser dito por qualquer um sobre qualquer coisa?", reescrever.

---

## Tracker — Consulta Obrigatória Antes de Propor

**Path do tracker:**
`/Users/joaopiccioni/Documents/Claude/Projects/LinkedIn & Instagram/hooks-utilizados.md`

O tracker registra qual padrão foi usado em cada post, quantas vezes, e marca padrões "queimados" pelo uso excessivo. Repetir padrão queimado dilui autenticidade percebida e treina o algoritmo a categorizar o autor como template, não como voz original.

**Workflow obrigatório no início de qualquer trabalho de hook:**

1. **Ler o tracker** com a tool Read.
2. **Mapear o estado dos padrões** — quais estão `livre`, quais têm baixo uso, quais estão `QUEIMADO`.
3. **Excluir os queimados** da proposta.
4. **Preferir padrões livres ou de baixo uso** quando houver mais de uma opção razoável.
5. **Se o tema só couber bem em um padrão de uso médio**, justificar explicitamente por que vale repetir.

Se o tracker não existir no path acima (sessão nova, projeto recém-aberto), avise o usuário e ofereça criar a estrutura básica antes de propor hook — sem tracker, a skill perde a memória que a torna útil.

---

## Biblioteca de Padrões

Cada padrão lista: *fórmula esquemática*, *exemplo validado*, *quando funciona melhor*, *armadilha comum*.

### 1. Tensão de Identidade

**Fórmula:** `[Palavra com duplo sentido ou carga emocional] + [de/dos + grupo específico]`

**Exemplo validado:** *"A alucinação dos C-levels."* → 3.628 impressões (vs. 256 do mesmo criador na mesma semana com hook informativo).

**Por que funciona:** nomeia um grupo identificável, usa palavra que ativa dois sentidos simultaneamente (técnico + metafórico), faz o leitor se perguntar "sou eu?". Qualquer pessoa do grupo-alvo sente pressão de clicar.

**Quando preferir:** maior alcance bruto. Posts que querem reach amplo sobre um grupo profissional reconhecível (founders, alocadores, analistas, C-levels, gestores).

**Armadilha:** se a palavra de duplo sentido não tem carga real, vira hook informativo disfarçado. *"O hábito dos investidores"* não funciona — não há tensão. *"A hipocrisia dos investidores"* funciona — tem julgamento embutido.

### 2. Distinção Analítica

**Fórmula:** `Há uma diferença entre [X] e [Y]. A maioria está fazendo o primeiro acreditando que está fazendo o segundo.`

**Exemplo:** *"Há uma diferença entre usar IA e comprimir assimetrias de informação com IA. A maioria das empresas está fazendo o primeiro acreditando que está fazendo o segundo."*

**Por que funciona:** cria tensão sem dramatismo, convida reflexão genuína, atrai comentários de pessoas que querem se diferenciar do grupo descrito. Ideal para perfis com voz analítica que evitam hipérbole.

**Quando preferir:** thought leadership analítico, leitura de mercado, distinções conceituais.

**Status no tracker do João:** `QUEIMADO`. Não usar até nova sinalização — o padrão foi explorado em excesso e perde efeito por reconhecimento de template.

### 3. Contrarian

**Fórmula:** afirmação direta contra o consenso do nicho, sem hedging.

**Exemplo:** *"A maioria dos analistas está olhando para o indicador errado."*

**Por que funciona:** ativa identificação imediata em quem concorda e provoca defesa em quem discorda — ambas viram comentário substantivo, que é o sinal forte para o 360Brew. Credibilidade técnica na pessoa que se posiciona.

**Quando preferir:** posts que apresentam tese própria contra leitura dominante. Funciona melhor com sustentação clara no corpo — sem evidência, vira opinião gratuita.

**Armadilha:** ser contrarian só por ser. O algoritmo (e o leitor) detecta contrarian gratuito e penaliza. A oposição precisa ser real e defensável.

### 4. Dado Específico

**Fórmula:** abre com número/dado preciso que ancora credibilidade, idealmente acompanhado de uma virada interpretativa.

**Exemplo:** *"Taxa de default de PMEs subiu 23% em Q1. O mercado não precificou."*

**Por que funciona:** número específico passa filtro de credibilidade do leitor em segundos. A virada na segunda frase ("o mercado não precificou") converte o dado em insight, não em estatística solta.

**Quando preferir:** posts ancorados em dados, análise quantitativa, leitura de mercado com evidência empírica. Forte para o pilar de mercados financeiros do João.

**Armadilha:** dado sem virada interpretativa é apenas notícia. *"VALE3 caiu 4% hoje."* não é hook — é manchete. Adicione a leitura: *"VALE3 caiu 4% hoje. O preço de minério já vinha sinalizando isso há duas semanas."*

### 5. Insight Pessoal

**Fórmula:** primeira pessoa com revelação acumulada por experiência específica.

**Exemplo:** *"Depois de 18 anos no mercado, aprendi que a tese mais perigosa é a que parece óbvia."*

**Por que funciona:** ativa autoridade via tempo + vulnerabilidade leve. O número de anos é o ancoragem; a revelação é a entrega.

**Quando preferir:** posts de storytelling com lição. Funciona bem para o pilar *practitioner-turned-builder* do João — combinar décadas de mercado com virada para AI-native.

**Armadilha:** abusar do "depois de X anos" vira tique. Use com moderação e varie a estrutura de tempo (não precisa ser sempre número de anos — pode ser evento, transição, decisão).

### 6. Pergunta Provocativa

**Fórmula:** pergunta reflexiva específica, não genérica, que reposiciona o problema.

**Exemplo:** *"Por que fundos com track record de 5 anos entregam menos alfa que fundos novatos?"*

**Por que funciona:** pergunta específica obriga o cérebro a tentar responder antes de continuar lendo. Reposiciona o problema — convida o leitor a pensar diferente.

**Quando preferir:** posts educacionais ou de framework, em que o corpo entrega a resposta de forma estruturada.

**Armadilha:** perguntas genéricas ("O que você acha sobre IA no mercado?") não funcionam — não obrigam pensamento. Tem que ser pergunta que o leitor sente que não sabe responder com facilidade.

### 7. Promessa de Framework

**Fórmula:** anunciar método próprio com número de etapas explícito.

**Exemplo:** *"O framework que uso para avaliar risco de crédito em 3 etapas:"*

**Por que funciona:** sinaliza save-worthy logo no início. Quem vê hook de framework e tem interesse marca para revisitar — saves valem 5-10x mais que likes no 360Brew.

**Quando preferir:** posts educacionais, conteúdo proprietário com nome próprio, IPs do João (Exército de Agentes, Capital Pulse).

**Armadilha:** prometer framework e entregar prosa. Se o corpo não tem estrutura numerada e clara, o hook vira clickbait. Frameworks pedem entregabilidade visual.

### 8. Profecia / Analogia Histórica

**Fórmula:** afirmação sobre o futuro ancorada em referência canônica do nicho.

**Exemplo:** *"A próxima Renaissance Technologies vai começar com cinco pessoas, dois MacBooks e GitHub aberto."* → usado em 2026-05-08, 96 caracteres.

**Por que funciona:** referência canônica (Renaissance em quant, Lehman em crise, Long-Term Capital em risco) ativa associação imediata em quem é do nicho. Cria curiosidade sem dramatismo. Sustenta voz analítica.

**Quando preferir:** posts visionários de tese, posicionamento como construtor declarando rota.

**Armadilha:** referência precisa ser universalmente reconhecida no público-alvo. Citar empresa que só especialistas conhecem perde a alavancagem; citar empresa óbvia demais (Apple, Microsoft) banaliza. O ponto doce é "todo mundo do nicho conhece, ninguém de fora liga".

### 9. Timestamp Transformation

**Fórmula:**
`[Ano]: [ponto baixo específico]`
`[Ano atual]: [ponto alto no mesmo domínio]`

**Exemplo:** *"2019: liquidando posição na bolsa para manter a equipe paga. 2026: alocando pessoalmente em teses de AI infrastructure."*

**Por que funciona:** dois timestamps geram um curiosity gap automático ("como?"). O leitor preenche o arco narrativo incompleto sozinho — não precisa ser empurrado.

**Quando preferir:** posts de transformação real e verificável. Pilar *practitioner-turned-builder* do João é território natural.

**Armadilha:** transformação inventada ou amplificada quebra confiança. Só usar quando há virada concreta documentável. Também: usar com moderação — se vira recurso recorrente, perde o impacto narrativo.

### 10. FOMO Insider

**Fórmula:** `Estamos diante de [oportunidade grande com referência histórica]. Se você está vendo esse post, está à frente de [percentual] do [público].`

**Exemplo:** *"Estamos diante da maior janela de reposicionamento de capital desde 2008. Se você está vendo esse post, está à frente de 95% dos alocadores brasileiros."*

**Por que funciona:** ativa FOMO sem soar clickbait quando o tema é genuinamente relevante. Combina urgência temporal + sinal de pertencimento ao grupo "à frente".

**Quando preferir:** posts sobre momentos de mercado reais com janela de oportunidade identificável.

**Armadilha:** se a promessa não é entregue no corpo (sem tese concreta, sem dado, sem ângulo novo), o algoritmo pune como hook enganoso. É o padrão com maior risco de clickbait penalty.

---

## Biblioteca de Templates Específicos por Categoria

Os 10 padrões acima são **arquétipos** com armadilha específica. Esta seção traz **templates prontos** por categoria — esqueletos com lacunas em colchetes para preencher. Quanto mais específico o preenchimento, melhor o hook performa. São complementares aos padrões: muitos templates encaixam em mais de um padrão (ex: um template de Story pode ser ao mesmo tempo Insight Pessoal e Timestamp Transformation).

### Curiosity (5 templates)

- *"Depois de [N] anos fazendo [prática comum], descobri por que a maioria dos [audiência] nunca [outcome]."*
- *"O jeito como a maioria dos [audiência] aborda [tema] é a razão de continuarem travados em [problema]."*
- *"Um [cliente/parceiro] me contou algo na semana passada sobre [tema] que eu nunca tinha considerado."*
- *"Existe uma razão pela qual seu [coisa] continua [problema], e não tem nada a ver com [suposição comum]."*
- *"Eu acreditava em [crença comum]. Aí [evento específico] aconteceu e hoje vejo isso de forma completamente diferente."*

### Contrarian (5 templates)

- *"Todo mundo diz que você precisa de [conselho comum] para conseguir [outcome]. Eu construí [prova] fazendo o oposto."*
- *"O conselho de [prática comum] é a pior coisa que se pode dar a um [audiência] iniciante."*
- *"A maioria das pessoas que ensinam [tema] online nunca de fato fez isso."*
- *"Eu discordo de quase todo conselho de [tema] circulando no LinkedIn agora."*
- *"Você não precisa de [requisito comum] para [outcome]. Eu construí [prova específica] sem nada disso."*

### Story (5 templates)

- *"Três anos atrás eu estava [ponto baixo]. Hoje eu rodo [outcome contrastante]. O que mudou no meio."*
- *"Um founder que assessorei mês passado chegou com [problema]. Em [período] tinha [outcome]. Como aconteceu."*
- *"A primeira vez que tentei [coisa], perdi [perda específica]. A segunda me ensinou algo que hoje compartilho com todo cliente."*
- *"Ontem alguém me perguntou como fui de [situação antiga] para [situação atual]. A resposta começa em um momento de [ano]."*
- *"Quase desisti de [coisa] em [ano]. Aí [pessoa específica] me disse algo que nunca esqueci."*

### Listicle (5 templates)

- *"Cinco coisas que eu queria ter ouvido antes de começar [tema]."*
- *"Três hábitos que silenciosamente mataram meu [outcome] nos primeiros dois anos."*
- *"Sete perguntas que faço a todo [audiência] antes de aceitar trabalhar junto."*
- *"Quatro sinais de que você está pronto para [próximo passo], e um sinal de que você não está."*
- *"Os seis conselhos que daria ao meu eu mais novo sobre construir [coisa]."*

### Transformation (5 templates)

- *"Seis meses atrás eu não conseguia [skill]. Hoje eu [outcome]. A virada veio de uma única mudança específica."*
- *"Meu [métrica] foi de [número baixo] para [número alto] em [período]. O que de fato moveu o ponteiro."*
- *"Saí de [situação anterior] para [situação atual] fazendo o trabalho não-glamoroso que ninguém comenta."*
- *"O eu de dois anos atrás não reconheceria o negócio que eu rodo hoje."*
- *"Minha primeira [coisa] gerou [outcome baixo]. Minha mais recente gerou [outcome alto]. A diferença é uma única skill."*

### Question (5 templates)

- *"O que separa os [audiência] que [têm sucesso] dos que ficam travados por anos?"*
- *"Por que tantos [audiência] confundem estar ocupado com fazer progresso real?"*
- *"Quando foi a última vez que seu [coisa] de fato moveu o ponteiro do seu negócio?"*
- *"Como seria seu [coisa] se você parasse de perseguir [prática comum] amanhã?"*
- *"Onde você vai estar em doze meses se nada na sua abordagem atual mudar?"*

### Como usar os templates

São **esqueletos**, não hooks finais. Trocar os colchetes por especificidade real do João: nomes de empresas que ele conhece (Renaissance Technologies, Stratechery), métricas que ele acompanha, datas verificáveis da carreira, públicos nomeados (alocador de FIA, gestor de FIM, head de research em casa de análise). Quanto mais o hook poderia ser dito apenas pelo João, melhor performa.

Os templates **não substituem o tracker** — escolher template ainda é escolha de padrão (Story → Insight Pessoal ou Timestamp Transformation; Contrarian → padrão Contrarian; Curiosity → Distinção Analítica ou Pergunta Provocativa). Antes de propor, validar contra o tracker.

---

## Anti-Padrões — Não Usar

**Estruturas "Não X, mas Y".** *"Não é sobre IA, mas sobre quem usa IA."* Soa como template, reduz autenticidade percebida. O João tem histórico de evitar contraposição explícita por preferência narrativa de acumulação — esse padrão entra em conflito direto com a voz dele.

**Afirmações paralelas que exigem processamento antes de gerar reação.** *"A NVIDIA criou X. Os LLMs criaram Y."* Pode ser interessante intelectualmente, mas não provoca ação imediata — o cérebro precisa parar para conectar antes de continuar.

**Hooks puramente informativos sem tensão.** *"A Anthropic lançou um modelo novo."* — comentário de notícia, baixíssima autoridade percebida pelo algoritmo. O 360Brew lê como repetição de feed RSS, não como contribuição original.

**Perguntas genéricas.** *"O que você pensa sobre isso?"* — vago demais para o cérebro engajar. Sempre nomear contexto, setor ou variável específica.

**Hooks > 210 caracteres.** Cortam no "Ver mais" e perdem a tensão. Sempre validar contagem antes de aprovar.

---

## Diagnóstico de Hook Fraco

Quando o usuário trouxer um hook para revisar, rodar este checklist:

1. **Cabe nos 210 caracteres?** Contar literalmente, incluindo espaços e pontuação.
2. **Sinaliza o tema explicitamente?** Audit semântico do 360Brew exige saber do que o post trata sem precisar do corpo.
3. **Cria curiosity gap genuíno ou artificial?** Genuíno: leitor quer saber porque o conteúdo é relevante. Artificial: leitor sente que está sendo manipulado.
4. **A promessa do hook é entregue no corpo?** Promessa ≠ entrega = clickbait penalty automático.
5. **Encaixa em algum dos 10 padrões?** Se não encaixa em nenhum, provavelmente é informativo demais.
6. **Está usando padrão queimado no tracker?** Se sim, propor alternativa em padrão livre.
7. **Soa como voz do João ou como template de IA?** Se for IA, ativar `linkedin-voice-joao` para recalibrar.
8. **Tem estrutura "Não X, mas Y" ou afirmações paralelas?** Se sim, reescrever em padrão direto.

---

## Workflow de Proposta de Hook

Quando o usuário pedir um hook (criação ou alternativa para post existente):

1. **Ler o tracker** em `/Users/joaopiccioni/Documents/Claude/Projects/LinkedIn & Instagram/hooks-utilizados.md`.
2. **Mapear padrões disponíveis** — listar livres, baixo uso, queimados.
3. **Entender o post** — pilar temático, tipo no mix (educacional/história/lead magnet/conversão), objetivo, tom desejado.
4. **Propor 1 hook principal** — padrão escolhido com justificativa explícita ("escolhido porque o tema X pede tensão sobre o grupo Y, e padrão Tensão de Identidade está livre no tracker").
5. **Propor 2-3 alternativas** em padrões diferentes — para o usuário escolher tom/ângulo.
6. **Validar contagem de caracteres** em cada opção.
7. **Indicar armadilhas específicas** se o tema flertar com clickbait penalty ou com voz template.

Formato de output sugerido:

```markdown
## Hook proposto (principal)

**Padrão:** [nome do padrão]
**Hook:** "[texto]"
**Caracteres:** [N]
**Por quê:** [justificativa em 1-2 frases]

## Alternativas

### Alternativa 1 — [padrão]
"[texto]" ([N] chars)
*Quando preferir: [contexto].*

### Alternativa 2 — [padrão]
"[texto]" ([N] chars)
*Quando preferir: [contexto].*

### Alternativa 3 — [padrão]
"[texto]" ([N] chars)
*Quando preferir: [contexto].*
```

---

## Atualização do Tracker Após Aprovação

Quando o usuário aprovar um hook e o post for publicado (ou pelo menos finalizado), atualizar o tracker:

1. **Incrementar o contador** do padrão usado na tabela.
2. **Atualizar a coluna "Última vez"** com a data do post.
3. **Adicionar entrada no Histórico** com:
   - Data + tema
   - Padrão usado
   - Texto do hook
   - Contagem de caracteres
   - Por quê (justificativa de uma frase)
   - Posicionamento do post
   - Link para o arquivo do post no projeto
4. **Marcar como `QUEIMADO`** se o contador passar de uso considerado saudável (ajustar com o usuário caso a caso, mas referência: 5-7 usos próximos no tempo já queimam).

Use a tool Edit para atualizar o tracker. Se o usuário disser que ainda não publicou, perguntar se quer registrar como rascunho ou esperar a publicação para atualizar.

---

## Adicionando Novos Padrões

Quando um padrão novo emergir na prática (variação que funcionou de modo diferente dos 10 listados), atualizar duas coisas:

1. **O tracker** — adicionar nova linha na tabela "Padrões — Contador de Uso" e descrição na seção "Padrões adicionais".
2. **Esta skill** — adicionar o padrão na biblioteca acima, com fórmula, exemplo validado, quando preferir e armadilha.

A skill cresce com a prática. Padrões viram artefatos consultáveis quando documentados; padrões mantidos só na cabeça desaparecem.

---

## Notas de Voz para o João

O João tem voz analítica, evita hipérbole, prefere acumulação narrativa a contraposição explícita, sustenta credibilidade via dados específicos e narrativa *practitioner-turned-builder*. Hooks que combinam com isso: Tensão de Identidade, Dado Específico, Insight Pessoal (quando ancorado em anos de mercado), Profecia/Analogia Histórica, Timestamp Transformation, Promessa de Framework (quando o framework é dele).

Hooks que conflitam com a voz dele: estruturas "Não X, mas Y" (queimadas pelo histórico), afirmações puramente provocativas sem sustentação, FOMO Insider sem dado real (risco de soar guru de growth).

Para calibração final de voz, ative `linkedin-voice-joao` (quando criada).
