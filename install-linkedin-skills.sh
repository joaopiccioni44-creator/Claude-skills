#!/bin/bash

# install-linkedin-skills.sh
# Instala a suíte de skills LinkedIn no Mac atual.
# Idempotente — pode ser rodado múltiplas vezes sem duplicar nada.
#
# Uso (em qualquer máquina, JobThinker ou JPThinker):
#   1. cd ~/Claude-skills && git pull origin main
#   2. ./install-linkedin-skills.sh

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

REPO_ROOT="$HOME/Claude-skills"
CLAUDE_SKILLS_DIR="$HOME/.config/claude/skills"

LINKEDIN_SKILLS=(
  "linkedin-360brew"
  "linkedin-hooks"
  "linkedin-post-doctor"
  "linkedin-voice-joao"
  "linkedin-templates"
  "linkedin-mix"
  "linkedin-carousel"
  "linkedin-newsletter-bridge"
  "linkedin-engajamento"
)

echo -e "${BLUE}=== Instalação da suíte LinkedIn ===${NC}"
echo -e "${BLUE}Máquina: $(hostname -s)${NC}"
echo ""

# ============================================================
# Etapa 1 — Copiar skills do repo para ~/.config/claude/skills/
# ============================================================
echo -e "${BLUE}[1/3] Copiando skills para ~/.config/claude/skills/...${NC}"

mkdir -p "$CLAUDE_SKILLS_DIR"

for skill in "${LINKEDIN_SKILLS[@]}"; do
  src="$REPO_ROOT/user-skills/$skill"
  dst="$CLAUDE_SKILLS_DIR/$skill"

  if [ ! -d "$src" ]; then
    echo -e "  ${RED}✗ $skill — fonte não encontrada em $src${NC}"
    continue
  fi

  # Remove versão antiga se existir (para evitar arquivos órfãos)
  if [ -d "$dst" ]; then
    rm -rf "$dst"
  fi

  cp -r "$src" "$dst"
  echo -e "  ${GREEN}✓ $skill${NC}"
done

echo ""

# ============================================================
# Etapa 2 — Detectar e atualizar CLAUDE.md global
# ============================================================
echo -e "${BLUE}[2/3] Localizando CLAUDE.md global...${NC}"

CLAUDE_MD_CANDIDATES=(
  "$HOME/.claude/CLAUDE.md"
  "$HOME/Library/Application Support/Claude/CLAUDE.md"
  "$HOME/.config/claude/CLAUDE.md"
)

CLAUDE_MD=""
for candidate in "${CLAUDE_MD_CANDIDATES[@]}"; do
  if [ -f "$candidate" ]; then
    CLAUDE_MD="$candidate"
    echo -e "  ${GREEN}✓ Encontrado em: $CLAUDE_MD${NC}"
    break
  fi
done

if [ -z "$CLAUDE_MD" ]; then
  echo -e "  ${YELLOW}⚠ CLAUDE.md global não encontrado nos paths padrão.${NC}"
  echo -e "  ${YELLOW}Adicione manualmente os imports abaixo no seu CLAUDE.md global:${NC}"
  echo ""
  for skill in "${LINKEDIN_SKILLS[@]}"; do
    echo "    @$REPO_ROOT/user-skills/$skill/SKILL.md"
  done
  echo ""
else
  added=0
  skipped=0
  for skill in "${LINKEDIN_SKILLS[@]}"; do
    import_line="@$REPO_ROOT/user-skills/$skill/SKILL.md"
    if grep -qF "$import_line" "$CLAUDE_MD"; then
      skipped=$((skipped + 1))
    else
      echo "" >> "$CLAUDE_MD"
      echo "$import_line" >> "$CLAUDE_MD"
      added=$((added + 1))
      echo -e "  ${GREEN}+ Adicionado: $skill${NC}"
    fi
  done

  if [ $added -eq 0 ]; then
    echo -e "  ${YELLOW}Todas as skills já estavam importadas (skipped: $skipped).${NC}"
  else
    echo -e "  ${GREEN}Total adicionado: $added | Já existentes: $skipped${NC}"
  fi
fi

echo ""

# ============================================================
# Etapa 3 — Aviso final
# ============================================================
echo -e "${BLUE}[3/3] Concluído.${NC}"
echo ""
echo -e "${GREEN}✓ Suíte LinkedIn instalada em $CLAUDE_SKILLS_DIR${NC}"

# Lembrete sobre o conflito com o plugin oficial
if command -v claude &>/dev/null; then
  echo ""
  echo -e "${YELLOW}Lembrete:${NC} se você tem o plugin 'anthropic-skills' instalado, a versão"
  echo -e "${YELLOW}'anthropic-skills:linkedin-360brew' (325 linhas) ainda vai competir pelo${NC}"
  echo -e "${YELLOW}auto-trigger com a sua versão local. Considere desabilitar via:${NC}"
  echo -e "${YELLOW}  claude /plugin → desabilitar anthropic-skills:linkedin-360brew${NC}"
fi

echo ""
echo -e "${GREEN}Próximo passo: reinicie o Claude Code para carregar as novas skills.${NC}"
