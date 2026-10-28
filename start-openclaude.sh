#!/bin/bash

export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

if ! command -v bun &> /dev/null; then
    echo "📦 Instalar Bun..."
    curl -fsSL https://bun.sh/install | bash
    export PATH="$BUN_INSTALL/bin:$PATH"
fi

if [ ! -f "/workspaces/openclaude/dist/cli.mjs" ]; then
    echo "🏗️ Compilando OpenClaude..."
    bun run build
fi

if ! pgrep -x "ollama" > /dev/null; then
    echo "🦙 Iniciando servidor Ollama..."
    ollama serve > /dev/null 2>&1 &
    sleep 2
fi

echo "🚀 Iniciando OpenClaude..."
bun run /workspaces/openclaude/dist/cli.mjs "$@"
