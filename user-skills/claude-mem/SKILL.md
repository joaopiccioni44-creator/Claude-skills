# Claude-Mem Skill

## Propósito

Esta skill ensina o Claude a usar e configurar o **claude-mem**, um sistema de memória persistente que captura automaticamente ações durante sessões de codificação, comprime com IA e reutiliza em futuras sessões.

## O que é Claude-Mem?

Plugin para Claude Code que mantém continuidade de conhecimento sobre projetos mesmo após sessões terminarem. Funciona automaticamente em background.

**Benefícios:**
- Memória persistente entre sessões
- Compressão inteligente de contexto
- Busca semântica no histórico
- Interface web para visualização

## Instalação

```bash
# 1. No Claude Code, execute:
/plugin marketplace add thedotmack/claude-mem

# 2. Instalar o plugin:
/plugin install claude-mem

# 3. Reiniciar Claude Code
```

O contexto de sessões anteriores aparecerá automaticamente nas novas sessões.

## Requisitos

- Node.js 18.0.0+
- Claude Code (versão recente)
- Bun (instalado automaticamente)
- uv para busca vetorial (instalado automaticamente)
- SQLite 3 (bundled)

## Ferramentas MCP de Busca

O claude-mem usa um workflow de 3 camadas para economizar tokens:

### Camada 1: `search`
Busca no índice compacto (~50-100 tokens/resultado):

```javascript
search(query="bug de autenticação", type="bugfix", limit=10)
// Retorna IDs e resumos
```

### Camada 2: `timeline`
Contexto cronológico ao redor de resultados:

```javascript
timeline(id=123, before=5, after=5)
// Mostra observações antes e depois
```

### Camada 3: `get_observations`
Detalhes completos de IDs específicos:

```javascript
get_observations(ids=[123, 456])
// Retorna conteúdo completo
```

### Workflow Típico

```
1. search(query="como implementei auth")
   → Retorna: #123, #456, #789

2. Revisar resumos, filtrar relevantes

3. get_observations(ids=[123, 456])
   → Detalhes completos para usar
```

## Interface Web

Visualizador em tempo real disponível em:

```
http://localhost:37777
```

Permite:
- Ver observações capturadas
- Buscar no histórico
- Monitorar compressão

## Configuração

Arquivo: `~/.claude-mem/settings.json`

```json
{
  "model": "claude-sonnet-4-20250514",
  "workerPort": 37777,
  "dataDir": "~/.claude-mem/data",
  "logLevel": "info",
  "contextInjection": {
    "enabled": true,
    "maxTokens": 4000
  }
}
```

## Privacidade

Use tags `<private>` para excluir conteúdo sensível:

```markdown
<private>
API_KEY=sk-xxxxx
Senha do banco: xxxxx
</private>
```

Conteúdo dentro dessas tags não será armazenado.

## Citações

Referencie observações passadas usando IDs:

```
Conforme observação #123, o bug foi causado por...
```

## Canal Beta

Para recursos experimentais (como Endless Mode):

```bash
/plugin update claude-mem --channel beta
```

## Troubleshooting

### Plugin não carrega

```bash
# Verificar instalação
ls ~/.claude/plugins/claude-mem

# Reinstalar
/plugin uninstall claude-mem
/plugin install claude-mem
```

### Interface web não abre

```bash
# Verificar porta
lsof -i :37777

# Reiniciar worker
/plugin restart claude-mem
```

### Memória não persiste

```bash
# Verificar diretório de dados
ls ~/.claude-mem/data

# Verificar logs
cat ~/.claude-mem/logs/latest.log
```

## Recursos

- **GitHub**: https://github.com/thedotmack/claude-mem
- **Docs**: https://docs.claude-mem.ai
- **Discord**: https://discord.com/invite/J4wttp9vDu
- **Twitter**: [@Claude_Memory](https://x.com/Claude_Memory)

## Licença

GNU Affero General Public License v3.0 (AGPL-3.0)
