# Build brief — migrar skills de LinkedIn de @import estático para descoberta sob demanda

Você está otimizando custo/contexto do Claude Code. NÃO é um bug funcional — é uma
mudança de mecanismo de carregamento. Leia a seção de Contexto inteira antes de
mexer em qualquer arquivo. Trabalho cirúrgico: mover + anotar frontmatter, não
reescrever conteúdo de skill nenhuma.

---

## Contexto (por que isso importa)

O arquivo `~/.claude/CLAUDE.md` (global, carregado em toda sessão do Claude Code,
em qualquer projeto, nesta conta) importa 11 arquivos via `@caminho/SKILL.md`:

```
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-360brew/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/infographic-prompt/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/metodo-falar/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-hooks/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-post-doctor/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-voice-joao/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-templates/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-mix/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-carousel/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-newsletter-bridge/SKILL.md
@/Users/joaopiccioni/Claude-skills/user-skills/linkedin-engajamento/SKILL.md
```

`@import` é **eager**: o conteúdo inteiro desses 11 arquivos é concatenado no
system prompt de **toda sessão**, mesmo quando a sessão não tem nada a ver com
LinkedIn (ex: uma sessão de código no AirPoint/Tom). Medido em 06/07/2026:

| Métrica | Valor |
|---|---|
| Tamanho somado dos 11 arquivos | 139.135 chars (~34.783 tokens) |
| Maior arquivo individual | `linkedin-hooks/SKILL.md` — 21.760 chars (~5.440 tok) |
| Sessões afetadas | 100% — qualquer projeto, em JPThinker (esta máquina) |
| Custo estimado desperdiçado | ~US$ 70 só de cache-read do Fable, só numa semana (01-06/07) — recorrente, todo dia, para sempre, em todos os modelos |

Contexto adicional que torna isso mais urgente: `~/.claude/settings.json` tem
`"model": "claude-fable-5[1m]"` como default — ou seja, mesmo sessões triviais
carregam esse overhead na tarifa mais cara disponível na conta.

## O mecanismo certo já existe e já funciona nesta conta — não é experimental

`~/.claude/settings.json` tem `"skillListingBudgetFraction": 0.03` — o Claude Code
já reserva uma fração pequena e fixa do contexto para uma *listagem leve* (nome +
description) de skills, e só carrega o conteúdo completo de uma skill quando ela é
de fato invocada pela tool `Skill`. Isso é o oposto do `@import`: é **lazy**.

Prova de que já está funcionando em produção nesta mesma conta:
`~/.claude/skills/01-cinematic/SKILL.md` (e os outros `0N-*` do plugin de vídeo),
`~/.claude/skills/_gstack-command/SKILL.md`. Ambos ficam em `~/.claude/skills/<nome>/SKILL.md`
com frontmatter YAML no topo:

```yaml
---
name: seedance-cinematic
description: Generate cinematic film-style video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants cinematic, film-like, movie-quality... Triggers on: cinematic, film look, movie scene, dramatic lighting...
---
```

A `description` é o que o roteador de skills usa pra decidir, sem carregar o corpo
inteiro, se aquela skill bate com o pedido do usuário. Quanto mais rica e
específica a description (sinônimos, gatilhos, quando usar), melhor o discovery.

Não existe nenhuma config adicional (`skillDirs` ou similar) em `settings.json` —
`~/.claude/skills/` é convenção fixa, sempre escaneada. Copiar uma pasta pra lá é
suficiente, nenhum registro manual necessário.

---

## TAREFA 1 — Adicionar frontmatter a cada uma das 11 skills

Para cada um dos 11 arquivos `SKILL.md` em `~/Claude-skills/user-skills/<nome>/`,
adicionar um bloco YAML no topo (ANTES do `# Título` atual), no formato:

```yaml
---
name: <nome-da-skill, igual ao nome da pasta>
description: <2-4 frases em inglês ou português, cobrindo: o que a skill faz,
  quando usar (gatilhos explícitos), e para quem/que tipo de pedido>
---
```

Não alterar nada do corpo do arquivo abaixo do frontmatter. A `description` deve
ser escrita a partir do conteúdo real de cada skill (já lido nesta conta antes,
resuma fielmente) — não inventar escopo que a skill não cobre. Usar como
referência de tom as descriptions dos exemplos do Seedance acima (específicas,
com lista de gatilhos, "use whenever...").

As 11 skills e uma pista de conteúdo pra cada description (ler o arquivo inteiro
antes de escrever a description final, isso aqui é só orientação):

- `linkedin-360brew` — núcleo conceitual + roteador para as demais skills de
  LinkedIn (360Brew, algoritmo, estrutura de 6 seções, roteamento pra skills
  satélite). Deixar claro na description que esta é o ponto de entrada quando o
  pedido for genérico ("me ajuda com um post de LinkedIn", "estratégia de
  LinkedIn") e as outras são para jobs específicos.
- `linkedin-hooks` — criar/revisar hooks (gancho, primeiras linhas) de posts.
- `linkedin-post-doctor` — revisar/pontuar post pronto (scoring /60).
- `linkedin-voice-joao` — calibrar voz autoral + filtro anti-AI-tells, usado como
  passada final em qualquer texto (não só LinkedIn).
- `linkedin-templates` — aplicar esqueleto persuasivo (PASTOR, Identity Upgrade,
  Advice I Ignored).
- `linkedin-mix` — decidir proporção 50/25/15/10 de tipos de post, auditar mix.
- `linkedin-carousel` — estrutura e workflow de carrossel LinkedIn (PDF
  multi-slide).
- `linkedin-newsletter-bridge` — divulgar newsletter sem sofrer bridge penalty.
- `linkedin-engajamento` — estratégia de comentários e engajamento, não geração
  de post.
- `infographic-prompt` — gerar prompts de infográfico (Nano Banana, Ideogram) —
  NÃO é específico de LinkedIn, é usado em qualquer conteúdo visual.
- `metodo-falar` — roteirista pelo Método F.A.L.A.R. (vídeo/palestra) — também
  não é específico de LinkedIn.

## TAREFA 2 — Mover as pastas para `~/.claude/skills/`

Depois do frontmatter estar em todas as 11, mover (não copiar) cada pasta inteira:

```
~/Claude-skills/user-skills/<nome>/  →  ~/.claude/skills/<nome>/
```

Preservar todo o conteúdo de cada pasta. Checado em 07/07: a maioria tem só
`SKILL.md`, mas 3 têm arquivo extra — mover a pasta inteira, não só o SKILL.md:

- `linkedin-360brew/` — 3 arquivos: `SKILL.md`, `_pre-refactor-backup.md` (conteúdo
  legado, referenciado no próprio SKILL.md como fallback pras skills-satélite que
  ainda não existem — manter), `CLAUDE.md` (artefato do claude-mem, ambiente
  automático, pode ficar ou ir, não é conteúdo de skill real).
- `infographic-prompt/` e `metodo-falar/` — 2 arquivos cada: `SKILL.md` +
  `CLAUDE.md` (mesmo artefato do claude-mem, idem acima).

Nota: `~/Claude-skills/user-skills/` tem ~30 pastas no total (canvas-design,
remotion, yc-advisor, etc.) — só as 11 desta lista estão em escopo. Não mexer
nas demais.

## TAREFA 3 — Remover as 11 linhas de @import do `~/.claude/CLAUDE.md`

Antes de editar: copiar `~/.claude/CLAUDE.md` para `~/.claude/CLAUDE.md.bak-pre-skill-migration`
(rollback barato). Depois, remover as 11 linhas `@/Users/joaopiccioni/Claude-skills/user-skills/.../SKILL.md`.
NÃO tocar em mais nada do arquivo (o bloco `<claude-mem-context>` no topo fica
como está).

## TAREFA 4 — Verificar se o mesmo problema existe no JobThinker (a outra máquina)

`~/.claude/CLAUDE.md` no JobThinker (`ssh jo@100.89.86.47`) é um arquivo
**independente**, não sincronizado com o desta máquina (2170 bytes lá vs 1169
aqui, conteúdo pode divergir). Não assumir que tem os mesmos 11 imports — ler
`ssh jo@100.89.86.47 "cat ~/.claude/CLAUDE.md"` primeiro. Se tiver o mesmo padrão
de @import de skills pesadas, repetir as tarefas 1-3 lá (as skills em si podem
já existir em `~/Claude-skills` do JobThinker também — conferir antes de
duplicar).

---

## Validação (fazer antes de apagar as pastas antigas)

1. **Skill descoberta continua funcionando:** abrir uma sessão nova e pedir algo
   que devia acionar uma skill específica (ex: "revisa esse hook de LinkedIn: ...").
   Confirmar que a skill certa é invocada via tool `Skill` (não mais via conteúdo
   já presente no system prompt).
2. **Roteador ainda funciona:** `linkedin-360brew` tem uma tabela de roteamento
   pras skills satélite (linkedin-hooks, linkedin-post-doctor, etc). Pedir algo
   genérico de LinkedIn e confirmar que o roteamento pra skill certa ainda
   acontece corretamente quando `linkedin-360brew` é carregada sob demanda (não
   mais pré-carregada).
3. **Overhead realmente caiu:** abrir uma sessão nova SEM nenhum pedido
   relacionado a LinkedIn/conteúdo (ex: uma pergunta trivial de código) e
   comparar o `input_tokens`/`cache_creation_input_tokens` da primeira mensagem
   do transcript (`~/.claude/projects/<projeto>/<sessionId>.jsonl`, campo
   `message.usage`) contra uma sessão antiga do mesmo tipo, de antes da migração.
   Esperado: queda de ~35k tokens na base.
4. Só depois de 1-3 confirmados: apagar `~/Claude-skills/user-skills/` (as 11
   pastas antigas) e o arquivo `.bak` de CLAUDE.md.

## O que NÃO fazer

- Não reescrever o conteúdo/lógica de nenhuma skill — só frontmatter + mover.
- Não tocar nos outros arquivos do `~/.claude/CLAUDE.md` além das 11 linhas de
  import.
- Não assumir que o JobThinker tem o mesmo problema sem checar primeiro.
- Não apagar as pastas antigas antes de validar o discovery funcionando.
- Não confundir isto com a estratégia de tiering de modelo (Fable vs Sonnet) —
  são otimizações diferentes, discutidas em outra sessão. Esta tarefa é só
  higiene de contexto.

## Output esperado

Ao final, listar:
- As 11 skills com frontmatter adicionado (confirmar description de cada uma).
- Confirmação de que `~/.claude/skills/<nome>/` tem as 11 pastas.
- Diff do `~/.claude/CLAUDE.md` (antes/depois).
- Resultado da Validação 3 (tokens antes vs depois) em número.
- Se JobThinker tinha o mesmo padrão: o que foi feito lá também.
