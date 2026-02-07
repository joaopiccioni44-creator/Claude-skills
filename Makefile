.PHONY: help sync install status update clean test

# Configurações
SKILLS_DIR := /mnt/skills/user
REPO_DIR := $(shell pwd)

# Cores para output
GREEN := \033[0;32m
YELLOW := \033[1;33m
NC := \033[0m

help: ## Mostra esta mensagem de ajuda
	@echo "$(GREEN)Claude Skills Repository - Comandos Disponíveis:$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""

sync: ## Sincroniza skills locais com GitHub
	@echo "$(GREEN)Sincronizando skills...$(NC)"
	@./sync-skills.sh

install: ## Instala skills do GitHub para máquina local
	@echo "$(GREEN)Instalando skills...$(NC)"
	@./install-skills.sh

status: ## Mostra status do repositório Git
	@echo "$(GREEN)Status do repositório:$(NC)"
	@git status
	@echo ""
	@echo "$(GREEN)Últimos commits:$(NC)"
	@git log --oneline -5

update: ## Atualiza repositório local com mudanças remotas
	@echo "$(GREEN)Atualizando repositório...$(NC)"
	@git pull origin main

clean: ## Remove arquivos temporários
	@echo "$(GREEN)Limpando arquivos temporários...$(NC)"
	@find . -name "*.tmp" -delete
	@find . -name "*.log" -delete
	@find . -name ".DS_Store" -delete
	@echo "$(GREEN)Limpeza concluída!$(NC)"

test: ## Testa se os scripts estão funcionando
	@echo "$(GREEN)Testando scripts...$(NC)"
	@echo "$(YELLOW)Verificando sync-skills.sh...$(NC)"
	@bash -n sync-skills.sh && echo "✓ Sintaxe OK" || echo "✗ Erro de sintaxe"
	@echo "$(YELLOW)Verificando install-skills.sh...$(NC)"
	@bash -n install-skills.sh && echo "✓ Sintaxe OK" || echo "✗ Erro de sintaxe"
	@echo ""
	@echo "$(YELLOW)Verificando permissões...$(NC)"
	@test -x sync-skills.sh && echo "✓ sync-skills.sh executável" || echo "✗ sync-skills.sh não executável"
	@test -x install-skills.sh && echo "✓ install-skills.sh executável" || echo "✗ install-skills.sh não executável"

list: ## Lista todas as skills no repositório
	@echo "$(GREEN)Skills disponíveis no repositório:$(NC)"
	@echo ""
	@find user-skills -maxdepth 1 -mindepth 1 -type d -exec basename {} \; | sort | while read skill; do \
		echo "  • $$skill"; \
	done

info: ## Mostra informações sobre o repositório
	@echo "$(GREEN)Informações do Repositório$(NC)"
	@echo ""
	@echo "Diretório: $(REPO_DIR)"
	@echo "Branch atual: $$(git branch --show-current)"
	@echo "Remote URL: $$(git config --get remote.origin.url)"
	@echo "Total de skills: $$(find user-skills -maxdepth 1 -mindepth 1 -type d | wc -l)"
	@echo "Último commit: $$(git log -1 --pretty=format:'%h - %s (%ar)')"

backup: ## Cria backup do repositório
	@echo "$(GREEN)Criando backup...$(NC)"
	@BACKUP_FILE="claude-skills-backup-$$(date +%Y%m%d-%H%M%S).tar.gz"; \
	tar -czf ../$$BACKUP_FILE .; \
	echo "$(GREEN)Backup criado: $$BACKUP_FILE$(NC)"

validate: ## Valida estrutura das skills
	@echo "$(GREEN)Validando estrutura das skills...$(NC)"
	@for skill_dir in user-skills/*; do \
		if [ -d "$$skill_dir" ]; then \
			skill_name=$$(basename "$$skill_dir"); \
			echo -n "  Validando $$skill_name... "; \
			if [ -f "$$skill_dir/SKILL.md" ]; then \
				echo "$(GREEN)✓$(NC)"; \
			else \
				echo "$(YELLOW)⚠ SKILL.md faltando$(NC)"; \
			fi; \
		fi; \
	done

diff: ## Mostra diferenças não commitadas
	@echo "$(GREEN)Diferenças não commitadas:$(NC)"
	@git diff

log: ## Mostra histórico de commits
	@git log --oneline --graph --decorate --all -20

branches: ## Lista todas as branches
	@echo "$(GREEN)Branches disponíveis:$(NC)"
	@git branch -a

# Atalhos
s: sync
i: install
u: update
st: status
