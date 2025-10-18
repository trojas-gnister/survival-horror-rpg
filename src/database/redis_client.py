"""Redis client for session management and caching."""

from typing import Optional, Any
import redis
from redis import Redis

from src.utils.config import settings


class RedisClient:
    """Redis client wrapper for Final Transmission game."""

    def __init__(self):
        self._client: Optional[Redis] = None

    def connect(self) -> None:
        """
        Connect to Redis using settings from config.

        START HERE:
        1. Create a Redis client using redis.Redis()
        2. Pass host, port, db, and decode_responses=True
        3. Store in self._client
        4. Test connection with ping()
        5. Handle any connection errors

        Docs: https://redis-py.readthedocs.io/en/stable/
        """
        # TODO: Implement Redis connection
        pass

    def disconnect(self) -> None:
        """
        Close Redis connection.

        START HERE:
        1. Check if self._client exists
        2. Call self._client.close()
        3. Set self._client to None
        """
        # TODO: Implement disconnect logic
        pass

    @property
    def client(self) -> Redis:
        """
        Get Redis client instance.

        START HERE:
        1. Check if self._client exists, if not raise an error
        2. Return self._client
        """
        # TODO: Implement client property
        raise NotImplementedError("Redis connection not established")

    def get(self, key: str) -> Optional[str]:
        """
        Get value from Redis.

        START HERE:
        1. Use self.client.get(key)
        2. Return the value
        3. Handle any errors

        Args:
            key: Redis key

        Returns:
            Value or None if key doesn't exist
        """
        # TODO: Implement get method
        pass

    def set(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """
        Set value in Redis.

        START HERE:
        1. Use self.client.set(key, value, ex=expire)
        2. Return True if successful
        3. Handle any errors

        Args:
            key: Redis key
            value: Value to store
            expire: Expiration time in seconds (optional)

        Returns:
            True if successful
        """
        # TODO: Implement set method
        return False

    def delete(self, key: str) -> bool:
        """
        Delete key from Redis.

        START HERE:
        1. Use self.client.delete(key)
        2. Return True if deleted
        3. Handle any errors

        Args:
            key: Redis key

        Returns:
            True if deleted
        """
        # TODO: Implement delete method
        return False

    def health_check(self) -> bool:
        """
        Check if Redis connection is healthy.

        START HERE:
        1. Try to ping Redis (self.client.ping())
        2. Return True if successful
        3. Return False if error occurs
        """
        # TODO: Implement health check
        return False


# Global Redis client instance
redis_client = RedisClient()
