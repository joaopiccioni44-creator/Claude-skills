# OpenClaw Docker Setup

Containerized deployment for OpenClaw.

## Quick Start

```bash
# Clone repository
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# Start with Docker Compose
docker-compose up -d
```

## Docker Compose Configuration

```yaml
version: '3.8'

services:
  openclaw:
    image: openclaw/openclaw:latest
    container_name: openclaw-gateway
    restart: unless-stopped
    ports:
      - "18789:18789"
    volumes:
      - ~/.openclaw:/root/.openclaw
      - ./workspace:/root/.openclaw/workspace
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN}
    networks:
      - openclaw-network

networks:
  openclaw-network:
    driver: bridge
```

## Environment File

Create `.env` in project root:

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-...

# Optional - Channels
TELEGRAM_BOT_TOKEN=123456:ABCDEF
DISCORD_BOT_TOKEN=...
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...

# Optional - Integrations
GITHUB_TOKEN=ghp_...
OPENAI_API_KEY=sk-...
```

## Building Custom Image

```dockerfile
FROM node:22-slim

WORKDIR /app

# Install OpenClaw
RUN npm install -g openclaw@latest

# Create config directory
RUN mkdir -p /root/.openclaw

# Copy configuration
COPY openclaw.json /root/.openclaw/openclaw.json

# Expose gateway port
EXPOSE 18789

# Start gateway
CMD ["openclaw", "gateway", "--port", "18789"]
```

Build and run:
```bash
docker build -t my-openclaw .
docker run -d \
  --name openclaw \
  -p 18789:18789 \
  -v ~/.openclaw:/root/.openclaw \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  my-openclaw
```

## Sandbox Mode with Docker

For running agent tools in isolated containers:

```json
{
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "non-main",
        "docker": {
          "image": "openclaw/sandbox:latest",
          "network": "openclaw-network",
          "setupCommand": "apt-get update && apt-get install -y python3 python3-pip"
        }
      }
    }
  }
}
```

## Docker Compose with Sandbox

```yaml
version: '3.8'

services:
  openclaw:
    image: openclaw/openclaw:latest
    container_name: openclaw-gateway
    restart: unless-stopped
    ports:
      - "18789:18789"
    volumes:
      - ~/.openclaw:/root/.openclaw
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    networks:
      - openclaw-network

  sandbox:
    image: openclaw/sandbox:latest
    container_name: openclaw-sandbox
    network_mode: "none"
    volumes:
      - sandbox-data:/workspace
    profiles:
      - sandbox

volumes:
  sandbox-data:

networks:
  openclaw-network:
    driver: bridge
```

## Useful Commands

```bash
# View logs
docker logs -f openclaw-gateway

# Enter container
docker exec -it openclaw-gateway /bin/bash

# Restart gateway
docker restart openclaw-gateway

# Update to latest
docker pull openclaw/openclaw:latest
docker-compose up -d

# Run doctor inside container
docker exec openclaw-gateway openclaw doctor
```

## Networking Considerations

### Expose to Tailnet

```yaml
services:
  openclaw:
    # ...
    environment:
      - GATEWAY_TAILSCALE_MODE=serve
```

### Behind Reverse Proxy (nginx)

```nginx
server {
    listen 443 ssl http2;
    server_name openclaw.yourdomain.com;

    location / {
        proxy_pass http://localhost:18789;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Troubleshooting

### Container won't start

```bash
# Check logs
docker logs openclaw-gateway

# Verify config
docker exec openclaw-gateway cat /root/.openclaw/openclaw.json
```

### Channel connection issues

```bash
# Check channel status
docker exec openclaw-gateway openclaw channels status

# Re-authenticate (WhatsApp)
docker exec -it openclaw-gateway openclaw channels login
```

### Permission issues

```bash
# Fix volume permissions
sudo chown -R 1000:1000 ~/.openclaw
```
