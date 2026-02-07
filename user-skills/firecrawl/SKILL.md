# Firecrawl Skill

## Propósito

Esta skill ensina o Claude a usar o Firecrawl para web scraping inteligente e extração de dados estruturados.

## Configuração

```bash
# API Key necessária
export FIRECRAWL_API_KEY="fc-xxxxx"
```

## Operações Disponíveis

### 1. Scrape (Página Única)

Extrai conteúdo de uma URL específica:

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com",
    "formats": ["markdown", "html"]
  }'
```

### 2. Crawl (Site Completo)

Navega recursivamente por um site:

```bash
curl -X POST https://api.firecrawl.dev/v1/crawl \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com",
    "limit": 100,
    "scrapeOptions": {
      "formats": ["markdown"]
    }
  }'
```

### 3. Extract (Dados Estruturados)

Extrai dados usando schema:

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/product",
    "formats": ["extract"],
    "extract": {
      "schema": {
        "type": "object",
        "properties": {
          "title": {"type": "string"},
          "price": {"type": "number"},
          "description": {"type": "string"}
        }
      }
    }
  }'
```

### 4. Search

Busca semântica na web:

```bash
curl -X POST https://api.firecrawl.dev/v1/search \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Brazilian tech startups 2025",
    "limit": 10
  }'
```

## Casos de Uso

### Monitoramento de RI (Relações com Investidores)

```python
# Extrair dados de releases de resultados
companies = ["VALE3", "PETR4", "ITUB4"]
for ticker in companies:
    url = f"https://ri.{ticker.lower()}.com.br"
    # scrape e extrair dados financeiros
```

### Coleta de Preços (E-commerce)

```python
# Monitorar preços de produtos
schema = {
    "type": "object",
    "properties": {
        "product_name": {"type": "string"},
        "price": {"type": "number"},
        "availability": {"type": "boolean"}
    }
}
```

## Boas Práticas

1. **Rate Limiting**: Respeitar limites da API
2. **Cache**: Armazenar resultados para evitar re-scraping
3. **Robots.txt**: Verificar se scraping é permitido
4. **Estruturação**: Usar schemas para dados consistentes

## Documentação

- Firecrawl Docs: https://docs.firecrawl.dev
- API Reference: https://docs.firecrawl.dev/api-reference
