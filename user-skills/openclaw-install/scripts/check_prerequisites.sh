#!/bin/bash
# OpenClaw Prerequisites Check Script
# Verifies system readiness for OpenClaw installation

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🦞 OpenClaw Prerequisites Check"
echo "================================"
echo ""

ERRORS=0
WARNINGS=0

# Check Node.js
echo -n "Checking Node.js... "
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version | sed 's/v//')
    NODE_MAJOR=$(echo $NODE_VERSION | cut -d. -f1)
    if [ "$NODE_MAJOR" -ge 22 ]; then
        echo -e "${GREEN}✓ v$NODE_VERSION${NC}"
    else
        echo -e "${RED}✗ v$NODE_VERSION (requires v22+)${NC}"
        ((ERRORS++))
    fi
else
    echo -e "${RED}✗ Not installed${NC}"
    ((ERRORS++))
fi

# Check npm
echo -n "Checking npm... "
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✓ v$NPM_VERSION${NC}"
else
    echo -e "${RED}✗ Not installed${NC}"
    ((ERRORS++))
fi

# Check pnpm (optional but recommended)
echo -n "Checking pnpm... "
if command -v pnpm &> /dev/null; then
    PNPM_VERSION=$(pnpm --version)
    echo -e "${GREEN}✓ v$PNPM_VERSION${NC}"
else
    echo -e "${YELLOW}○ Not installed (optional, recommended)${NC}"
    ((WARNINGS++))
fi

# Check Git
echo -n "Checking Git... "
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version | sed 's/git version //')
    echo -e "${GREEN}✓ v$GIT_VERSION${NC}"
else
    echo -e "${YELLOW}○ Not installed (needed for source builds)${NC}"
    ((WARNINGS++))
fi

# Check Docker (optional)
echo -n "Checking Docker... "
if command -v docker &> /dev/null; then
    DOCKER_VERSION=$(docker --version | sed 's/Docker version //' | cut -d, -f1)
    echo -e "${GREEN}✓ v$DOCKER_VERSION${NC}"
else
    echo -e "${YELLOW}○ Not installed (optional, for sandbox mode)${NC}"
    ((WARNINGS++))
fi

# Check available disk space
echo -n "Checking disk space... "
if command -v df &> /dev/null; then
    AVAILABLE_GB=$(df -BG ~ | tail -1 | awk '{print $4}' | sed 's/G//')
    if [ "$AVAILABLE_GB" -ge 2 ]; then
        echo -e "${GREEN}✓ ${AVAILABLE_GB}GB available${NC}"
    else
        echo -e "${YELLOW}○ ${AVAILABLE_GB}GB available (recommend 2GB+)${NC}"
        ((WARNINGS++))
    fi
else
    echo -e "${YELLOW}○ Could not check${NC}"
fi

# Check if port 18789 is available
echo -n "Checking port 18789... "
if command -v lsof &> /dev/null; then
    if lsof -i :18789 &> /dev/null; then
        echo -e "${YELLOW}○ In use (gateway may conflict)${NC}"
        ((WARNINGS++))
    else
        echo -e "${GREEN}✓ Available${NC}"
    fi
elif command -v netstat &> /dev/null; then
    if netstat -tuln 2>/dev/null | grep -q ":18789 "; then
        echo -e "${YELLOW}○ In use (gateway may conflict)${NC}"
        ((WARNINGS++))
    else
        echo -e "${GREEN}✓ Available${NC}"
    fi
else
    echo -e "${YELLOW}○ Could not check${NC}"
fi

# Check OpenClaw installation status
echo ""
echo "OpenClaw Status:"
echo -n "  Installed... "
if command -v openclaw &> /dev/null; then
    OC_VERSION=$(openclaw --version 2>/dev/null || echo "unknown")
    echo -e "${GREEN}✓ $OC_VERSION${NC}"
else
    echo -e "${YELLOW}○ Not yet installed${NC}"
fi

# Summary
echo ""
echo "================================"
if [ $ERRORS -eq 0 ]; then
    if [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✓ All prerequisites met!${NC}"
        echo ""
        echo "Ready to install:"
        echo "  npm install -g openclaw@latest"
        echo "  openclaw onboard --install-daemon"
    else
        echo -e "${YELLOW}○ $WARNINGS warning(s), but can proceed${NC}"
        echo ""
        echo "You can install now:"
        echo "  npm install -g openclaw@latest"
    fi
else
    echo -e "${RED}✗ $ERRORS error(s) found${NC}"
    echo ""
    echo "Fix the errors above before installing."
    echo ""
    echo "To install Node.js 22:"
    echo "  # Using nvm (recommended)"
    echo "  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"
    echo "  nvm install 22"
    echo "  nvm use 22"
    exit 1
fi
