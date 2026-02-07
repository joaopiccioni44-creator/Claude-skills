# Guia de Setup Inicial - Claude Skills Repository

Este documento guia você através do processo de configuração inicial do seu repositório de skills do Claude.

## 📦 Conteúdo do Export

Você recebeu uma estrutura completa com:

```
skills-export/
├── .gitignore              # Configuração Git
├── README.md               # Documentação principal
├── SKILL_TEMPLATE.md       # Template para novas skills
├── sync-skills.sh          # Script de upload (máquina → GitHub)
├── install-skills.sh       # Script de download (GitHub → máquina)
├── skills-manifest.json    # Índice de metadados
└── openclaw-install/       # Skill de exemplo
    ├── SKILL.md
    ├── references/
    │   ├── channels.md
    │   ├── configuration.md
    │   └── docker-setup.md
    └── scripts/
        ├── check_prerequisites.sh
        └── quick_install.sh
```

## 🚀 Passo a Passo de Configuração

### 1. Download dos Arquivos

Primeiro, baixe e extraia os arquivos exportados do Claude:

```bash
# Os arquivos estão em /home/claude/skills-export/
# Você pode baixá-los usando o present_files do Claude
```

### 2. Preparar o Repositório GitHub

No seu terminal local (não no Claude):

```bash
# Navegue até onde você clonou o repositório
cd ~/caminho/para/Claude-skills

# Copie os arquivos exportados para o repositório
cp -r ~/Downloads/skills-export/* .

# Estrutura de diretórios
mkdir -p user-skills
mv openclaw-install user-skills/

# Tornar scripts executáveis
chmod +x sync-skills.sh install-skills.sh
```

### 3. Configurar Git

```bash
# Inicializar (se necessário)
git init

# Adicionar arquivos
git add .

# Primeiro commit
git commit -m "Initial commit: Setup Claude Skills repository

- Add openclaw-install skill
- Add sync and install automation scripts
- Add comprehensive README and documentation
- Add skills manifest and template"

# Conectar ao repositório remoto
git remote add origin https://github.com/joaopiccioni44-creator/Claude-skills.git

# Push inicial
git branch -M main
git push -u origin main
```

### 4. Testar Sincronização

```bash
# Teste o script de sync
./sync-skills.sh

# Você deve ver:
# - Detecção automática de skills em /mnt/skills/user
# - Cópia para user-skills/
# - Commit e push automáticos
```

### 5. Configurar em Outras Máquinas

Em cada máquina adicional:

```bash
# Clone o repositório
git clone https://github.com/joaopiccioni44-creator/Claude-skills.git
cd Claude-skills

# Torne os scripts executáveis
chmod +x *.sh

# Para instalar skills do repo no Claude
./install-skills.sh

# Para enviar novas skills desta máquina para o repo
./sync-skills.sh
```

## 🔧 Ajustes Necessários

### Script sync-skills.sh

Verifique se o caminho das skills está correto:

```bash
# Linha 16 do sync-skills.sh
SKILLS_SOURCE="/mnt/skills/user"
```

Se suas skills estão em outro local, ajuste este caminho.

### Script install-skills.sh

Ajuste o diretório de destino das skills:

```bash
# Linha 16 do install-skills.sh
CLAUDE_SKILLS_DIR="$HOME/.config/claude/skills"
```

Altere para o diretório correto onde o Claude lê as skills na sua máquina.

## 📝 Próximos Passos

### 1. Adicionar Novas Skills

Quando você criar uma nova skill no Claude:

```bash
# O script sync-skills.sh automaticamente:
# 1. Detecta novas skills em /mnt/skills/user
# 2. Copia para o repositório
# 3. Faz commit e push

./sync-skills.sh
```

### 2. Atualizar o Manifesto

Sempre que adicionar uma nova skill, atualize `skills-manifest.json`:

```json
{
  "name": "nome-da-nova-skill",
  "category": "categoria",
  "description": "Descrição detalhada",
  "triggers": ["palavra1", "palavra2"],
  "files": ["SKILL.md"],
  "tags": ["tag1", "tag2"],
  "last_updated": "2025-02-06"
}
```

### 3. Documentar Adequadamente

Use o `SKILL_TEMPLATE.md` como base para criar documentação consistente:

```bash
cp SKILL_TEMPLATE.md user-skills/minha-nova-skill/SKILL.md
# Edite o arquivo conforme necessário
```

## 🔄 Workflows Recomendados

### Workflow Diário

```bash
# Ao final do dia, sincronize suas skills
cd ~/Claude-skills
./sync-skills.sh
```

### Workflow de Nova Máquina

```bash
# 1. Clone o repositório
git clone https://github.com/joaopiccioni44-creator/Claude-skills.git

# 2. Instale as skills
cd Claude-skills
./install-skills.sh

# 3. Selecione "a" para instalar todas ou escolha específicas
```

### Workflow de Atualização

```bash
# Máquina A: fez mudanças
cd ~/Claude-skills
./sync-skills.sh

# Máquina B: quer as atualizações
cd ~/Claude-skills
git pull origin main
./install-skills.sh
```

## 🛡️ Segurança e Boas Práticas

1. **Nunca commitar credenciais:**
   - Use `.env` para secrets (já em .gitignore)
   - Revise cada commit antes de push

2. **Revisar mudanças:**
   ```bash
   git status
   git diff
   ```

3. **Mensagens de commit descritivas:**
   - O script sync-skills.sh permite customizar a mensagem
   - Use descrições claras do que foi alterado

4. **Backup regular:**
   - Configure sync automático via cron/launchd
   - Mantenha pelo menos um backup local

## 📊 Monitoramento

### Verificar Status do Repo

```bash
cd ~/Claude-skills
git status
git log --oneline -10
```

### Ver Histórico de Uma Skill

```bash
git log --follow -- user-skills/openclaw-install/SKILL.md
```

### Comparar Versões

```bash
# Ver mudanças desde último commit
git diff HEAD

# Ver mudanças de um commit específico
git show <commit-hash>
```

## 🆘 Troubleshooting

### Problema: Script não encontra skills

**Solução:**
```bash
# Verifique o caminho
ls -la /mnt/skills/user

# Ajuste SKILLS_SOURCE em sync-skills.sh se necessário
```

### Problema: Erro de permissão no Git

**Solução:**
```bash
# Configure suas credenciais Git
git config --global user.name "João Piccioni"
git config --global user.email "seu@email.com"

# Para GitHub, use Personal Access Token
```

### Problema: Conflitos de merge

**Solução:**
```bash
# Baixar mudanças remotas
git fetch origin

# Ver diferenças
git diff origin/main

# Resolver conflitos manualmente ou
git pull --rebase origin main
```

## 📚 Recursos Adicionais

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [Markdown Guide](https://www.markdownguide.org)

## ✅ Checklist de Setup

- [ ] Arquivos extraídos e copiados para repositório local
- [ ] Git inicializado e conectado ao remote
- [ ] Primeiro commit realizado
- [ ] Push para GitHub bem-sucedido
- [ ] Scripts tornados executáveis (chmod +x)
- [ ] Caminhos ajustados nos scripts
- [ ] Teste de sync-skills.sh realizado
- [ ] Teste de install-skills.sh realizado
- [ ] Manifesto atualizado com suas skills
- [ ] README personalizado (opcional)
- [ ] Backup configurado (opcional)

---

**Dúvidas?** Consulte o README.md ou abra uma issue no GitHub.

**Última atualização:** 06 de Fevereiro de 2025
