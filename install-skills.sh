#!/bin/bash

# Script de Instalação de Claude Skills
# Autor: João Piccioni
# Repositório: https://github.com/joaopiccioni44-creator/Claude-skills.git

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configurações
REPO_URL="https://github.com/joaopiccioni44-creator/Claude-skills.git"
LOCAL_REPO="$HOME/Claude-skills"
CLAUDE_SKILLS_DIR="$HOME/.config/claude/skills"  # Ajuste conforme necessário

echo -e "${GREEN}=== Claude Skills Installation ===${NC}"

# Verificar se o repositório já existe
if [ ! -d "$LOCAL_REPO" ]; then
    echo -e "${YELLOW}Clonando repositório...${NC}"
    git clone "$REPO_URL" "$LOCAL_REPO"
else
    echo -e "${YELLOW}Atualizando repositório...${NC}"
    cd "$LOCAL_REPO"
    git pull origin main
fi

cd "$LOCAL_REPO"

# Criar diretório de skills do Claude se não existir
mkdir -p "$CLAUDE_SKILLS_DIR"

# Listar skills disponíveis
echo -e "\n${BLUE}Skills disponíveis:${NC}"
skill_list=()
counter=1

if [ -d "user-skills" ]; then
    for skill_dir in user-skills/*; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            skill_list+=("$skill_name")
            
            # Verificar se já está instalada
            if [ -d "$CLAUDE_SKILLS_DIR/$skill_name" ]; then
                echo -e "  ${counter}. ${GREEN}$skill_name${NC} ${YELLOW}(instalada)${NC}"
            else
                echo -e "  ${counter}. $skill_name"
            fi
            ((counter++))
        fi
    done
else
    echo -e "${RED}Erro: Diretório user-skills não encontrado${NC}"
    exit 1
fi

# Menu de instalação
echo -e "\n${BLUE}Opções:${NC}"
echo "  a - Instalar todas as skills"
echo "  n - Instalar skill específica por número"
echo "  q - Sair"
echo ""
read -p "Escolha uma opção: " choice

case $choice in
    a|A)
        echo -e "${YELLOW}Instalando todas as skills...${NC}"
        for skill_name in "${skill_list[@]}"; do
            echo -e "  • Instalando: ${GREEN}$skill_name${NC}"
            cp -r "user-skills/$skill_name" "$CLAUDE_SKILLS_DIR/"
        done
        echo -e "${GREEN}✓ Todas as skills instaladas!${NC}"
        ;;
    q|Q)
        echo "Saindo..."
        exit 0
        ;;
    [0-9]*)
        if [ "$choice" -ge 1 ] && [ "$choice" -le "${#skill_list[@]}" ]; then
            skill_name="${skill_list[$((choice-1))]}"
            echo -e "${YELLOW}Instalando: ${GREEN}$skill_name${NC}"
            cp -r "user-skills/$skill_name" "$CLAUDE_SKILLS_DIR/"
            echo -e "${GREEN}✓ Skill instalada com sucesso!${NC}"
        else
            echo -e "${RED}Número inválido${NC}"
            exit 1
        fi
        ;;
    *)
        echo -e "${RED}Opção inválida${NC}"
        exit 1
        ;;
esac

# Mostrar skills instaladas
echo -e "\n${BLUE}Skills instaladas em $CLAUDE_SKILLS_DIR:${NC}"
ls -1 "$CLAUDE_SKILLS_DIR" | while read skill; do
    echo -e "  • ${GREEN}$skill${NC}"
done

echo -e "\n${GREEN}=== Instalação Completa ===${NC}"
echo -e "${YELLOW}Nota: Reinicie o Claude para carregar as novas skills${NC}"
