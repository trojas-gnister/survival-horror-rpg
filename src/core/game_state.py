"""Game state management."""

from typing import Optional
from bson import ObjectId

from src.models.game import GameModel, ResourcesModel
from src.database.mongodb_client import mongodb_client
from src.database.redis_client import redis_client
from src.utils.config import settings


class GameState:
    """
    Manages game state persistence and retrieval.

    START HERE:
    1. This class handles saving/loading game state
    2. Uses MongoDB for persistent storage
    3. Uses Redis for fast session data
    4. Coordinates between databases
    """

    def __init__(self):
        self.current_game: Optional[GameModel] = None
        self.current_resources: Optional[ResourcesModel] = None

    def create_new_game(self, player_name: str) -> GameModel:
        """
        Create a new game session.

        START HERE:
        1. Create a new GameModel with player_name
        2. Set initial values from settings (difficulty, etc.)
        3. Insert into MongoDB 'games' collection
        4. Create initial ResourcesModel
        5. Insert into MongoDB 'resources' collection
        6. Store game_id in Redis session
        7. Set self.current_game and self.current_resources
        8. Return the created game

        Args:
            player_name: Name of the player

        Returns:
            Created GameModel
        """
        # TODO: Implement create_new_game
        pass

    def load_game(self, game_id: str) -> Optional[GameModel]:
        """
        Load an existing game by ID.

        START HERE:
        1. Convert game_id string to ObjectId
        2. Query MongoDB 'games' collection
        3. Load corresponding resources from 'resources' collection
        4. Set self.current_game and self.current_resources
        5. Store game_id in Redis session
        6. Return the game or None if not found

        Args:
            game_id: Game ID string

        Returns:
            GameModel or None
        """
        # TODO: Implement load_game
        pass

    def save_game(self) -> bool:
        """
        Save current game state to MongoDB.

        START HERE:
        1. Check if self.current_game exists
        2. Update 'last_played' timestamp
        3. Update game document in MongoDB
        4. Update resources document in MongoDB
        5. Update Redis cache with latest values
        6. Return True if successful

        Returns:
            True if saved successfully
        """
        # TODO: Implement save_game
        return False

    def get_current_resources(self) -> Optional[ResourcesModel]:
        """
        Get current resource state.

        START HERE:
        1. Try to get from Redis first (fast)
        2. If not in Redis, get from self.current_resources
        3. If still None, query MongoDB
        4. Return the resources

        Returns:
            Current ResourcesModel or None
        """
        # TODO: Implement get_current_resources
        pass

    def update_resources(self, **kwargs) -> None:
        """
        Update resource values.

        START HERE:
        1. Get current resources
        2. Update fields from kwargs (fuel, sanity, battery, etc.)
        3. Clamp values to valid ranges (0-100, etc.)
        4. Save to MongoDB
        5. Update Redis cache

        Args:
            **kwargs: Resource fields to update
        """
        # TODO: Implement update_resources
        pass

    def advance_night(self) -> None:
        """
        Advance to the next night.

        START HERE:
        1. Increment self.current_game.current_night
        2. Decrease food by 1
        3. Apply nightly resource drain (fuel, etc.)
        4. Create new ResourcesModel entry for the night
        5. Check win/lose conditions
        6. Save game state

        """
        # TODO: Implement advance_night
        pass


# Global game state instance
game_state = GameState()
