#!/bin/bash
# Setup script for Final Transmission

set -e

echo "🎮 Final Transmission - Setup Script"
echo "===================================="
echo ""

# Check for Poetry
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry not found. Installing..."
    curl -sSL https://install.python-poetry.org | python3 -
    echo "✅ Poetry installed"
else
    echo "✅ Poetry found"
fi

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
else
    echo "✅ Docker found"
fi

# Check for Ollama
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama not found. Installing..."
    curl -fsSL https://ollama.com/install.sh | sh
    echo "✅ Ollama installed"
else
    echo "✅ Ollama found"
fi

# Install Python dependencies
echo ""
echo "📦 Installing Python dependencies..."
poetry install

# Copy .env file
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ .env created"
else
    echo "✅ .env already exists"
fi

# Start Docker services
echo ""
echo "🐳 Starting Docker services..."
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 5

# Pull Ollama model
echo ""
echo "🤖 Pulling Ollama model (qwen2:0.5b)..."
ollama pull qwen2:0.5b

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Quick start:"
echo "   poetry run python -m src.main test-connections  # Test connections"
echo "   poetry run python -m src.main play              # Start game"
echo ""
