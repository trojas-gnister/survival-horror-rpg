# Final Transmission

> AI-powered survival horror radio operator game

## 🎮 About

You're a night-shift radio operator in a remote facility. Strange transmissions come through. Make life-or-death decisions about who to trust, who to help, and who to ignore. Every choice has consequences. The AI remembers everything.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Poetry (`curl -sSL https://install.python-poetry.org | python3 -`)
- Docker & Docker Compose
- Ollama (`curl -fsSL https://ollama.com/install.sh | sh`)

### Setup

```bash
# 1. Install dependencies
poetry install

# 2. Copy environment file
cp .env.example .env

# 3. Start databases (MongoDB, Redis, Chroma)
docker-compose up -d

# 4. Pull Ollama model
ollama pull llama3.1:latest

# 5. Run the game
poetry run python -m src.main
```

## 🏗️ Tech Stack

- **Python 3.11** - Core language
- **Ollama** - Local LLM (llama3.1)
- **LlamaIndex** - RAG framework for AI memory
- **MongoDB** - Game state & data persistence
- **Chroma** - Vector database for semantic search
- **Redis** - Session management & caching
- **Rich** - Beautiful terminal UI
- **Pydantic** - Data validation

## 📝 License

MIT

---

Built by [trojas-gnister](https://github.com/trojas-gnister)
