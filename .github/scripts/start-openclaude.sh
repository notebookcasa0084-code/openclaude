#!/usr/bin/env bash
set -e

echo "[OpenClaude] Iniciando ambiente..."

# 1. Verificar se o Ollama está instalado
if ! command -v ollama &> /dev/null; then
    echo "[Erro] Ollama não encontrado. Instalando..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

# 2. Verificar se o servidor do Ollama já está rodando
if ! pgrep -x "ollama" > /dev/null; then
    echo "[Ollama] Iniciando o servidor em segundo plano..."
    mkdir -p ~/.openclaude/logs
    nohup ollama serve > ~/.openclaude/logs/ollama.log 2>&1 &
    sleep 3
else
    echo "[Ollama] O servidor já está em execução."
fi

echo "[OpenClaude] Ambiente pronto para uso!"
