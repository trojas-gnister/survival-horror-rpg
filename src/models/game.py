"""Game state models."""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    """Custom ObjectId type for Pydantic."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, _schema_generator):
        return {"type": "string"}


class GameModel(BaseModel):
    """
    Main game state model.

    START HERE:
    1. This model represents a single game session
    2. Stores in MongoDB 'games' collection
    3. Use this to track overall game progress
    4. Add any additional fields you need for your game
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    player_name: str
    current_night: int = 1
    game_status: str = "active"  # active, completed, game_over
    started_at: datetime = Field(default_factory=datetime.utcnow)
    last_played: datetime = Field(default_factory=datetime.utcnow)
    endings_unlocked: List[str] = Field(default_factory=list)
    difficulty: str = "normal"

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ResourcesModel(BaseModel):
    """
    Player resources model.

    START HERE:
    1. Tracks fuel, sanity, battery, food, trust
    2. Updated every game tick/night
    3. Stored in MongoDB 'resources' collection
    4. Link to game via game_id
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    game_id: PyObjectId
    night: int
    generator_fuel: float = 100.0  # 0-100
    radio_battery: float = 100.0  # 0-100
    sanity: float = 100.0  # 0-100
    food: int = 7  # days remaining
    trust_score: float = 0.0  # -100 to +100
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
