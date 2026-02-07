# OpenClaw Channel Setup Guide

Detailed setup instructions for each messaging channel.

## WhatsApp

### Setup

1. Run the login wizard:
   ```bash
   openclaw channels login
   ```

2. Scan the QR code with WhatsApp on your phone:
   - Open WhatsApp → Settings → Linked Devices → Link a Device

3. Configure allowlist in `~/.openclaw/openclaw.json`:
   ```json
   {
     "channels": {
       "whatsapp": {
         "allowFrom": ["+1234567890"]
       }
     }
   }
   ```

### Group Access

```json
{
  "channels": {
    "whatsapp": {
      "groups": ["*"],
      "groupActivation": "mention"
    }
  }
}
```

- `groups: ["*"]` allows all groups
- `groupActivation: "mention"` requires @mention to activate

### Troubleshooting

- **Session expired**: Run `openclaw channels login` again
- **Messages not received**: Check `allowFrom` list
- **Credentials location**: `~/.openclaw/credentials/whatsapp/`

---

## Telegram

### Setup

1. Create a bot via [@BotFather](https://t.me/BotFather):
   - Send `/newbot`
   - Follow prompts to get token

2. Configure:
   ```json
   {
     "channels": {
       "telegram": {
         "botToken": "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
       }
     }
   }
   ```

   Or via environment:
   ```bash
   export TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
   ```

### Group Configuration

```json
{
  "channels": {
    "telegram": {
      "groups": {
        "*": {
          "requireMention": true
        },
        "-1001234567890": {
          "requireMention": false
        }
      }
    }
  }
}
```

### Webhook Mode (Optional)

```json
{
  "channels": {
    "telegram": {
      "webhookUrl": "https://your-domain.com/webhook/telegram"
    }
  }
}
```

---

## Slack

### Setup

1. Create a Slack App at https://api.slack.com/apps

2. Enable Socket Mode:
   - Settings → Socket Mode → Enable
   - Generate App-Level Token with `connections:write` scope

3. Add Bot Token Scopes:
   - `app_mentions:read`
   - `channels:history`
   - `chat:write`
   - `im:history`
   - `im:write`
   - `users:read`

4. Install to workspace and get Bot Token

5. Configure:
   ```json
   {
     "channels": {
       "slack": {
         "botToken": "xoxb-...",
         "appToken": "xapp-..."
       }
     }
   }
   ```

### DM Policy

```json
{
  "channels": {
    "slack": {
      "dm": {
        "policy": "pairing",
        "allowFrom": ["U1234567890"]
      }
    }
  }
}
```

---

## Discord

### Setup

1. Create application at https://discord.com/developers/applications

2. Create Bot:
   - Bot → Add Bot
   - Copy token
   - Enable "Message Content Intent"

3. Generate invite URL:
   - OAuth2 → URL Generator
   - Scopes: `bot`, `applications.commands`
   - Permissions: Send Messages, Read Message History, etc.

4. Configure:
   ```json
   {
     "channels": {
       "discord": {
         "token": "your-bot-token"
       }
     }
   }
   ```

### Guild Configuration

```json
{
  "channels": {
    "discord": {
      "guilds": {
        "123456789012345678": {
          "channels": ["987654321098765432"],
          "requireMention": true
        }
      }
    }
  }
}
```

### DM Policy

```json
{
  "channels": {
    "discord": {
      "dm": {
        "policy": "pairing",
        "allowFrom": ["user-id-1", "user-id-2"]
      }
    }
  }
}
```

---

## Signal

### Prerequisites

Install `signal-cli`:
```bash
# macOS
brew install signal-cli

# Linux
# See: https://github.com/AsamK/signal-cli
```

### Setup

1. Register or link:
   ```bash
   signal-cli -u +1234567890 register
   # or link to existing account
   signal-cli link -n "OpenClaw"
   ```

2. Configure:
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

---

## iMessage

### Prerequisites

- macOS only
- Messages app signed in with Apple ID
- Full Disk Access for Terminal/IDE

### Setup

```json
{
  "channels": {
    "imessage": {
      "enabled": true,
      "allowFrom": ["+1234567890", "email@example.com"],
      "groups": ["*"]
    }
  }
}
```

### Troubleshooting

- Grant Full Disk Access: System Preferences → Security & Privacy → Privacy → Full Disk Access
- Ensure Messages.app is running

---

## Microsoft Teams

### Setup

1. Register app in Azure Portal
2. Create Bot Framework registration
3. Configure:
   ```json
   {
     "channels": {
       "msteams": {
         "appId": "...",
         "appPassword": "...",
         "allowFrom": ["user@org.com"],
         "groupPolicy": "pairing"
       }
     }
   }
   ```

---

## WebChat

Built-in web interface, no external setup required.

Access at: `http://localhost:18789` (when gateway is running)

---

## Security Best Practices

1. **Always use allowlists** for production
2. **Enable DM pairing** for unknown senders
3. **Run `openclaw doctor`** to check configuration
4. **Use environment variables** for tokens (not config files)
5. **Restrict gateway binding** to localhost unless using Tailscale
