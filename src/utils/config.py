"""Configuration management using pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # MongoDB
    mongodb_host: str = "localhost"
    mongodb_port: int = 27017
    mongodb_user: str = "admin"
    mongodb_password: str = "password"
    mongodb_database: str = "final_transmission"

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    # Chroma
    chroma_host: str = "localhost"
    chroma_port: int = 8000

    # Ollama
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen2:0.5b"

    # Game Configuration
    game_difficulty: str = "normal"
    max_nights: int = 14
    starting_fuel: float = 100.0
    starting_sanity: float = 100.0
    starting_battery: float = 100.0
    starting_food_days: int = 7

    # Logging
    log_level: str = "INFO"

    @property
    def mongodb_url(self) -> str:
        """Construct MongoDB connection URL."""
        return f"mongodb://{self.mongodb_user}:{self.mongodb_password}@{self.mongodb_host}:{self.mongodb_port}"

    @property
    def redis_url(self) -> str:
        """Construct Redis connection URL."""
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

    @property
    def chroma_url(self) -> str:
        """Construct Chroma connection URL."""
        return f"http://{self.chroma_host}:{self.chroma_port}"


# Global settings instance
settings = Settings()
