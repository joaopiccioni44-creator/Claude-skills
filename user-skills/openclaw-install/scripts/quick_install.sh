#!/bin/bash
# OpenClaw Quick Install Script
# Automated installation for OpenClaw

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo ""
echo -e "${BLUE}🦞 OpenClaw Quick Install${NC}"
echo "========================="
echo ""

# Parse arguments
CHANNEL="stable"
SKIP_DAEMON=false
USE_PNPM=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --channel)
            CHANNEL="$2"
            shift 2
            ;;
        --skip-daemon)
            SKIP_DAEMON=true
            shift
            ;;
        --pnpm)
            USE_PNPM=true
            shift
            ;;
        --help)
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  --channel <stable|beta|dev>  Install channel (default: stable)"
            echo "  --skip-daemon                Skip daemon installation"
            echo "  --pnpm                       Use pnpm instead of npm"
            echo "  --help                       Show this help"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Check Node.js version
echo -n "Checking Node.js... "
if ! command -v node &> /dev/null; then
    echo -e "${RED}✗ Not found${NC}"
    echo ""
    echo "Please install Node.js 22 or later:"
    echo "  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"
    echo "  source ~/.bashrc"
    echo "  nvm install 22"
    exit 1
fi

NODE_MAJOR=$(node --version | sed 's/v//' | cut -d. -f1)
if [ "$NODE_MAJOR" -lt 22 ]; then
    echo -e "${RED}✗ v$(node --version) (requires v22+)${NC}"
    echo ""
    echo "Please upgrade Node.js:"
    echo "  nvm install 22"
    echo "  nvm use 22"
    exit 1
fi
echo -e "${GREEN}✓ $(node --version)${NC}"

# Determine package manager
if [ "$USE_PNPM" = true ]; then
    if ! command -v pnpm &> /dev/null; then
        echo -n "Installing pnpm... "
        npm install -g pnpm
        echo -e "${GREEN}✓${NC}"
    fi
    PKG_MGR="pnpm"
    PKG_CMD="pnpm add -g"
else
    PKG_MGR="npm"
    PKG_CMD="npm install -g"
fi

# Determine package version based on channel
case $CHANNEL in
    stable)
        PACKAGE="openclaw@latest"
        ;;
    beta)
        PACKAGE="openclaw@beta"
        ;;
    dev)
        PACKAGE="openclaw@dev"
        ;;
    *)
        echo -e "${RED}Unknown channel: $CHANNEL${NC}"
        exit 1
        ;;
esac

# Install OpenClaw
echo ""
echo -e "${BLUE}Installing OpenClaw ($CHANNEL channel)...${NC}"
$PKG_CMD $PACKAGE

# Verify installation
echo ""
echo -n "Verifying installation... "
if command -v openclaw &> /dev/null; then
    echo -e "${GREEN}✓${NC}"
    openclaw --version
else
    echo -e "${RED}✗ Installation failed${NC}"
    exit 1
fi

# Run onboarding
if [ "$SKIP_DAEMON" = false ]; then
    echo ""
    echo -e "${BLUE}Running onboarding wizard...${NC}"
    echo ""
    openclaw onboard --install-daemon
else
    echo ""
    echo -e "${YELLOW}Skipping daemon installation.${NC}"
    echo "Run manually later: openclaw onboard --install-daemon"
fi

# Success message
echo ""
echo -e "${GREEN}═══════════════════════════════════════${NC}"
echo -e "${GREEN}🦞 OpenClaw installed successfully!${NC}"
echo -e "${GREEN}═══════════════════════════════════════${NC}"
echo ""
echo "Quick commands:"
echo "  openclaw gateway --verbose    # Start gateway"
echo "  openclaw doctor               # Health check"
echo "  openclaw channels login       # Setup WhatsApp"
echo "  openclaw --help               # Show all commands"
echo ""
echo "Documentation: https://docs.openclaw.ai"
echo ""
