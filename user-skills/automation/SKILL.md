# Automation Skill

## Propósito

Esta skill ensina o Claude a criar workflows automatizados usando n8n, Make.com e integrações de APIs.

## Plataformas Suportadas

### n8n (Self-hosted)

```bash
# Instalação via Docker
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### Make.com (Cloud)

- Dashboard: https://make.com
- API Docs: https://developers.make.com

## Padrões de Workflow

### 1. Multi-Agent Research Pipeline

```
[Trigger: Schedule/Webhook]
        ↓
[Perplexity: Search Query]
        ↓
[Claude: Analyze & Summarize]
        ↓
[Notion: Save Results]
        ↓
[Slack/Email: Notify]
```

### 2. Content Distribution

```
[Trigger: New Notion Page]
        ↓
[Claude: Adapt for Platform]
        ↓
[Parallel:]
  → [Twitter: Post Thread]
  → [LinkedIn: Post Article]
  → [Newsletter: Queue Email]
```

### 3. Data Pipeline

```
[Trigger: Daily Schedule]
        ↓
[Firecrawl: Scrape Sources]
        ↓
[Claude: Clean & Structure]
        ↓
[Database: Store]
        ↓
[Dashboard: Update]
```

## Templates n8n

### Webhook para Notion

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "notion-sync",
        "method": "POST"
      }
    },
    {
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "parameters": {
        "operation": "create",
        "databaseId": "{{$env.NOTION_DATABASE_ID}}"
      }
    }
  ]
}
```

## Integrações Comuns

| Serviço | Uso | API |
|---------|-----|-----|
| Notion | Database, Docs | REST API |
| Slack | Notificações | Webhooks |
| Perplexity | Research | REST API |
| Firecrawl | Scraping | REST API |
| SendGrid | Email | REST API |
| Airtable | Database | REST API |

## Boas Práticas

1. **Error Handling**: Sempre incluir tratamento de erros
2. **Logging**: Registrar execuções para debug
3. **Retry Logic**: Implementar retentativas para falhas
4. **Secrets**: Usar variáveis de ambiente para API keys
5. **Idempotência**: Garantir que re-execuções são seguras

## Exemplos de Uso

```
"Crie um workflow n8n que monitora o RSS do InfoMoney"
"Faça um pipeline que coleta dados do Twitter e salva no Notion"
"Automatize o envio de relatórios diários por email"
```
