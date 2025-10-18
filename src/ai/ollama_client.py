"""Ollama client for local LLM interactions."""

from typing import Optional, List, Dict, Any
import ollama

from src.utils.config import settings


class OllamaClient:
    """Ollama client wrapper for Final Transmission game."""

    def __init__(self):
        self._client: Optional[ollama.Client] = None

    def connect(self) -> None:
        """
        Initialize Ollama client.

        START HERE:
        1. Create ollama.Client() with host=settings.ollama_base_url
        2. Store in self._client
        3. Test by listing models (client.list())
        4. Handle any connection errors

        Docs: https://github.com/ollama/ollama-python
        """
        # TODO: Implement Ollama client initialization
        pass

    @property
    def client(self) -> ollama.Client:
        """
        Get Ollama client instance.

        START HERE:
        1. Check if self._client exists, if not raise an error
        2. Return self._client
        """
        # TODO: Implement client property
        raise NotImplementedError("Ollama client not initialized")

    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500,
    ) -> str:
        """
        Generate text from Ollama model.

        START HERE:
        1. Build messages list with system and user prompts
        2. Call self.client.chat() with model=settings.ollama_model
        3. Pass messages and options (temperature, num_predict=max_tokens)
        4. Extract response text from result
        5. Return the generated text
        6. Handle any errors

        Args:
            prompt: User prompt
            system: System prompt (optional)
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum tokens to generate

        Returns:
            Generated text
        """
        # TODO: Implement generate method
        return ""

    def generate_json(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.3,
    ) -> Dict[str, Any]:
        """
        Generate structured JSON from Ollama model.

        START HERE:
        1. Add "Output must be valid JSON" to system prompt
        2. Call self.generate() with the prompts
        3. Parse response as JSON using json.loads()
        4. Return the parsed JSON dict
        5. Handle JSON parsing errors

        Args:
            prompt: User prompt
            system: System prompt (optional)
            temperature: Sampling temperature (lower for structured output)

        Returns:
            Parsed JSON dict
        """
        # TODO: Implement generate_json method
        return {}

    def health_check(self) -> bool:
        """
        Check if Ollama is running and model is available.

        START HERE:
        1. Try to list models (self.client.list())
        2. Check if settings.ollama_model is in the list
        3. Return True if found
        4. Return False if error or model not found
        """
        # TODO: Implement health check
        return False


# Global Ollama client instance
ollama_client = OllamaClient()
