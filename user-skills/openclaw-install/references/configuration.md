# OpenClaw Configuration Reference

Complete configuration options for `~/.openclaw/openclaw.json`.

## Agent Configuration

```json
{
  "agent": {
    "model": "anthropic/claude-opus-4-5",
    "maxTokens": 4000,
    "thinkingLevel": "medium"
  },
  "agents": {
    "defaults": {
      "workspace": "~/.openclaw/workspace",
      "sandbox": {
        "mode": "non-main"
      }
    }
  }
}
```

### Thinking Levels

- `off` | `minimal` | `low` | `medium` | `high` | `xhigh`

## Gateway Configuration

```json
{
  "gateway": {
    "port": 18789,
    "bind": "127.0.0.1",
    "auth": {
      "mode": "token",
      "allowTailscale": true
    },
    "tailscale": {
      "mode": "off"
    }
  }
}
```

### Tailscale Modes

- `off`: No Tailscale automation (default)
- `serve`: Tailnet-only HTTPS
- `funnel`: Public HTTPS (requires password auth)

## Channel Configuration

### WhatsApp

```json
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["+1234567890", "+0987654321"],
      "groups": ["*"]
    }
  }
}
```

### Telegram

```json
{
  "channels": {
    "telegram": {
      "botToken": "123456:ABCDEF",
      "allowFrom": ["username1", "username2"],
      "groups": {
        "*": {
          "requireMention": true
        }
      }
    }
  }
}
```

### Slack

```json
{
  "channels": {
    "slack": {
      "botToken": "xoxb-...",
      "appToken": "xapp-...",
      "dm": {
        "policy": "pairing",
        "allowFrom": []
      }
    }
  }
}
```

### Discord

```json
{
  "channels": {
    "discord": {
      "token": "...",
      "dm": {
        "policy": "pairing",
        "allowFrom": []
      },
      "guilds": {},
      "mediaMaxMb": 25
    }
  }
}
```

### Signal

```json
{
  "channels": {
    "signal": {
      "enabled": true,
      "number": "+1234567890"
    }
  }
}
```

Requires `signal-cli` installed and configured.

### iMessage

```json
{
  "channels": {
    "imessage": {
      "enabled": true,
      "groups": ["*"]
    }
  }
}
```

macOS only. Messages app must be signed in.

## Browser Configuration

```json
{
  "browser": {
    "enabled": true,
    "color": "#FF4500",
    "headless": false
  }
}
```

## Skills Configuration

```json
{
  "skills": {
    "load": {
      "extraDirs": ["/path/to/custom/skills"],
      "watch": true
    }
  }
}
```

## Sandbox Configuration

```json
{
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "non-main",
        "docker": {
          "image": "openclaw/sandbox:latest",
          "setupCommand": "apt-get update && apt-get install -y python3"
        }
      }
    }
  }
}
```

### Sandbox Modes

- `off`: No sandboxing (tools run on host)
- `non-main`: Sandbox only group/channel sessions
- `all`: Sandbox all sessions

### Tool Allowlists (Sandbox)

Default allowed: `bash`, `process`, `read`, `write`, `edit`, `sessions_list`, `sessions_history`, `sessions_send`, `sessions_spawn`

Default denied: `browser`, `canvas`, `nodes`, `cron`, `discord`, `gateway`

## Environment Variables

These override config file settings:

```bash
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=123456:ABCDEF
DISCORD_BOT_TOKEN=...
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
GITHUB_TOKEN=ghp_...
```

## Multi-Agent Configuration

```json
{
  "agents": {
    "main": {
      "model": "anthropic/claude-opus-4-5",
      "workspace": "~/.openclaw/workspace/main"
    },
    "assistant": {
      "model": "anthropic/claude-sonnet-4-5",
      "workspace": "~/.openclaw/workspace/assistant"
    }
  }
}
```

Route channels to specific agents via channel configuration.
