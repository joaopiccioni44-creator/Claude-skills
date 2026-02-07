# Claude Skills Repository

> Repositório centralizado de skills customizadas para o Claude AI, mantido por João Piccioni

[![GitHub](https://img.shields.io/badge/GitHub-joaopiccioni44--creator-blue)](https://github.com/joaopiccioni44-creator)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Visão Geral

Este repositório serve como hub centralizado para gerenciar, versionar e compartilhar skills customizadas do Claude AI entre diferentes máquinas e projetos. As skills expandem as capacidades nativas do Claude com conhecimento especializado e fluxos de trabalho otimizados.

## 🗂 Estrutura do Repositório

```
Claude-skills/
├── user-skills/              # Skills customizadas de usuário
│   ├── openclaw-install/     # Instalação e setup do OpenClaw
│   │   ├── SKILL.md          # Documentação principal
│   │   ├── references/       # Docs de referência
│   │   │   ├── channels.md
│   │   │   ├── configuration.md
│   │   │   └── docker-setup.md
│   │   └── scripts/          # Scripts auxiliares
│   │       ├── check_prerequisites.sh
│   │       └── quick_install.sh
│   └── [outras-skills]/
├── sync-skills.sh            # Script de upload (local → GitHub)
├── install-skills.sh         # Script de download (GitHub → local)
├── skills-manifest.json      # Metadados e índice das skills
├── .gitignore               # Arquivos ignorados pelo Git
└── README.md                # Este arquivo
```

## 🚀 Quick Start

### Clonar o Repositório

```bash
git clone https://github.com/joaopiccioni44-creator/Claude-skills.git
cd Claude-skills
```

### Instalar Skills

```bash
# Tornar o script executável (primeira vez apenas)
chmod +x install-skills.sh

# Executar instalador interativo
./install-skills.sh
```

O script apresentará um menu para:
- Instalar todas as skills de uma vez
- Instalar skills específicas por número
- Visualizar quais skills já estão instaladas

### Sincronizar Skills Locais com GitHub

```bash
# Tornar o script executável (primeira vez apenas)
chmod +x sync-skills.sh

# Sincronizar skills
./sync-skills.sh
```

Este script:
1. Copia automaticamente todas as skills de `/mnt/skills/user` para o repositório
2. Detecta mudanças
3. Cria commit com timestamp
4. Faz push para o GitHub

## 📚 Skills Disponíveis

### openclaw-install

**Categoria:** Installation & Setup  
**Descrição:** Guia completo de instalação e configuração do OpenClaw, assistente pessoal de IA

**Recursos:**
- Instalação via NPM ou build from source
- Configuração de gateway (macOS/Linux/Docker)
- Setup de canais (WhatsApp, Telegram, Slack, Discord, Signal, iMessage)
- Troubleshooting e resolução de problemas
- Gerenciamento de skills e ClawdHub registry

**Pré-requisitos:**
- Node.js ≥ 22
- pnpm ou npm
- Git

**Plataformas:** macOS, Linux, Docker

---

*Mais skills serão adicionadas conforme o desenvolvimento*

## 🛠 Desenvolvimento e Contribuição

### Criando uma Nova Skill

1. **Criar estrutura de diretórios:**

```bash
cd user-skills
mkdir minha-nova-skill
cd minha-nova-skill
```

2. **Criar arquivo SKILL.md:**

```markdown
---
name: minha-nova-skill
description: Breve descrição do que a skill faz
---

# Minha Nova Skill

Documentação completa aqui...
```

3. **Adicionar ao manifesto:**

Edite `skills-manifest.json` e adicione entrada na array `skills`:

```json
{
  "name": "minha-nova-skill",
  "category": "categoria-apropriada",
  "description": "Descrição detalhada",
  "triggers": ["palavra-chave", "outra-palavra"],
  "files": ["SKILL.md"],
  "tags": ["tag1", "tag2"],
  "last_updated": "2025-02-06"
}
```

4. **Sincronizar com GitHub:**

```bash
./sync-skills.sh
```

### Boas Práticas

- **Documentação clara:** Cada skill deve ter um SKILL.md bem estruturado
- **Metadados completos:** Manter skills-manifest.json atualizado
- **Versionamento:** Usar mensagens de commit descritivas
- **Modularidade:** Separar documentação de referência em subdiretórios
- **Scripts auxiliares:** Incluir scripts úteis na pasta `scripts/`

## 🔄 Workflow de Sincronização

### Cenário 1: Adicionar Skills de uma Nova Máquina

```bash
# Na nova máquina
git clone https://github.com/joaopiccioni44-creator/Claude-skills.git
cd Claude-skills

# Copiar skills locais para o repo
./sync-skills.sh
```

### Cenário 2: Sincronizar Skills Entre Máquinas

```bash
# Máquina A: Upload de novas skills
./sync-skills.sh

# Máquina B: Download das atualizações
git pull origin main
./install-skills.sh
```

### Cenário 3: Backup Automático

Configure um cron job ou launchd para sync automático:

```bash
# Exemplo de cron (diário às 18h)
0 18 * * * cd ~/Claude-skills && ./sync-skills.sh
```

## 📊 Metadados das Skills

O arquivo `skills-manifest.json` mantém metadados estruturados sobre cada skill:

- **name:** Identificador único
- **category:** Categoria funcional (installation, finance, web-scraping, etc.)
- **description:** Descrição concisa
- **triggers:** Palavras-chave que ativam a skill
- **files:** Lista de arquivos incluídos
- **prerequisites:** Dependências necessárias
- **platforms:** Sistemas operacionais suportados
- **tags:** Tags para busca e organização
- **last_updated:** Data da última atualização

## 🎯 Casos de Uso

### Para Análise Financeira
- Skills de web scraping de dados de B3
- Frameworks de análise fundamentalista
- Integração com APIs de mercado

### Para Automação
- Configuração de workflows n8n/Make.com
- Scripts de integração de APIs
- Setups de multi-agent systems

### Para Desenvolvimento
- Guias de instalação de ferramentas
- Configurações de ambientes
- Best practices e padrões

## 🔐 Segurança

- **Nunca** commitar credenciais, API keys ou dados sensíveis
- Use `.env` para configurações locais (já incluído em .gitignore)
- Revise cada commit antes de fazer push
- Considere usar repositório privado para skills proprietárias

## 📝 Licença

MIT License - sinta-se livre para usar e modificar conforme necessário.

## 👤 Autor

**João Piccioni**
- GitHub: [@joaopiccioni44-creator](https://github.com/joaopiccioni44-creator)
- LinkedIn: [João Piccioni](https://linkedin.com/in/joaopiccioni)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:

1. Fork o repositório
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaNovaSkill`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova skill para X'`)
4. Push para a branch (`git push origin feature/MinhaNovaSkill`)
5. Abrir um Pull Request

## 📮 Suporte

Para questões ou sugestões:
- Abra uma [issue no GitHub](https://github.com/joaopiccioni44-creator/Claude-skills/issues)
- Entre em contato diretamente

---

**Última atualização:** 06 de Fevereiro de 2025  
**Versão:** 1.0.0
