"""MongoDB client for game state persistence."""

from typing import Optional
from pymongo import MongoClient
from pymongo.database import Database

from src.utils.config import settings


class MongoDBClient:
    """MongoDB client wrapper for Final Transmission game."""

    def __init__(self):
        self._client: Optional[MongoClient] = None
        self._db: Optional[Database] = None

    def connect(self) -> None:
        """
        Connect to MongoDB using settings from config.

        START HERE:
        1. Create a MongoClient using settings.mongodb_url
        2. Store it in self._client
        3. Get the database using settings.mongodb_database
        4. Store it in self._db
        5. Test connection with ping command
        6. Handle any connection errors

        Docs: https://pymongo.readthedocs.io/en/stable/tutorial.html
        """
        # TODO: Implement MongoDB connection
        pass

    def disconnect(self) -> None:
        """
        Close MongoDB connection.

        START HERE:
        1. Check if self._client exists
        2. Call self._client.close()
        3. Set self._client and self._db to None
        """
        # TODO: Implement disconnect logic
        pass

    @property
    def db(self) -> Database:
        """
        Get database instance.

        START HERE:
        1. Check if self._db exists, if not raise an error
        2. Return self._db
        """
        # TODO: Implement database property
        raise NotImplementedError("Database connection not established")

    def health_check(self) -> bool:
        """
        Check if MongoDB connection is healthy.

        START HERE:
        1. Try to ping the database (db.command('ping'))
        2. Return True if successful
        3. Return False if error occurs
        """
        # TODO: Implement health check
        return False


# Global MongoDB client instance
mongodb_client = MongoDBClient()
