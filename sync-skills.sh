#!/bin/bash

# Script de Sincronização de Claude Skills
# Autor: João Piccioni
# Repositório: https://github.com/joaopiccioni44-creator/Claude-skills.git

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configurações
REPO_URL="https://github.com/joaopiccioni44-creator/Claude-skills.git"
SKILLS_SOURCE="/mnt/skills/user"
LOCAL_REPO="$HOME/Claude-skills"

echo -e "${GREEN}=== Claude Skills Sync ===${NC}"

# Verificar se o repositório já existe
if [ ! -d "$LOCAL_REPO" ]; then
    echo -e "${YELLOW}Clonando repositório...${NC}"
    git clone "$REPO_URL" "$LOCAL_REPO"
else
    echo -e "${YELLOW}Atualizando repositório existente...${NC}"
    cd "$LOCAL_REPO"
    git pull origin main
fi

cd "$LOCAL_REPO"

# Criar estrutura de diretórios se não existir
mkdir -p user-skills

# Copiar skills do Claude para o repositório
echo -e "${YELLOW}Copiando skills...${NC}"

# Listar skills disponíveis
if [ -d "$SKILLS_SOURCE" ]; then
    for skill_dir in "$SKILLS_SOURCE"/*; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            echo -e "  • Copiando: ${GREEN}$skill_name${NC}"
            
            # Criar diretório da skill no repo
            mkdir -p "user-skills/$skill_name"
            
            # Copiar todos os arquivos
            cp -r "$skill_dir"/* "user-skills/$skill_name/"
        fi
    done
else
    echo -e "${RED}Erro: Diretório de skills não encontrado em $SKILLS_SOURCE${NC}"
    exit 1
fi

# Adicionar README se não existir
if [ ! -f "README.md" ]; then
    cat > README.md << 'EOF'
# Claude Skills Repository

Repositório centralizado de skills customizadas para o Claude AI.

## Estrutura

```
Claude-skills/
├── user-skills/          # Skills customizadas de usuário
│   ├── skill-name/
│   │   ├── SKILL.md      # Documentação principal da skill
│   │   ├── references/   # Documentação de referência
│   │   └── scripts/      # Scripts auxiliares
│   └── ...
└── README.md
```

## Como Usar

### Instalando Skills

1. Clone este repositório:
   ```bash
   git clone https://github.com/joaopiccioni44-creator/Claude-skills.git
   ```

2. Copie as skills desejadas para o diretório de skills do Claude em sua máquina

### Sincronizando Skills

Use o script `sync-skills.sh` para sincronizar automaticamente suas skills:

```bash
./sync-skills.sh
```

## Skills Disponíveis

As skills neste repositório incluem ferramentas para:
- Instalação e configuração de sistemas
- Automação de tarefas
- Análise financeira
- Web scraping
- E muito mais...

## Contribuindo

Para adicionar novas skills:
1. Crie um diretório em `user-skills/` com o nome da skill
2. Adicione um arquivo `SKILL.md` com a documentação
3. Commit e push suas mudanças

## Autor

João Piccioni - [GitHub](https://github.com/joaopiccioni44-creator)
EOF
fi

# Git add
echo -e "${YELLOW}Preparando commit...${NC}"
git add -A

# Verificar se há mudanças
if git diff --staged --quiet; then
    echo -e "${GREEN}Nenhuma mudança detectada. Tudo está sincronizado!${NC}"
else
    # Mostrar resumo das mudanças
    echo -e "${YELLOW}Mudanças detectadas:${NC}"
    git status --short
    
    # Criar mensagem de commit automática
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    COMMIT_MSG="Update skills - $TIMESTAMP"
    
    # Opção de customizar mensagem
    read -p "Mensagem de commit (Enter para usar padrão): " CUSTOM_MSG
    if [ ! -z "$CUSTOM_MSG" ]; then
        COMMIT_MSG="$CUSTOM_MSG"
    fi
    
    # Commit
    git commit -m "$COMMIT_MSG"
    
    # Push
    echo -e "${YELLOW}Enviando para GitHub...${NC}"
    git push origin main
    
    echo -e "${GREEN}✓ Skills sincronizadas com sucesso!${NC}"
fi

echo -e "${GREEN}=== Sincronização Completa ===${NC}"
