"""Game event models."""

from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from bson import ObjectId

from src.models.game import PyObjectId


class EventModel(BaseModel):
    """
    World event model.

    START HERE:
    1. Represents things that happen in the game world
    2. Can be triggered by player choices or ambient
    3. Affects game state and resources
    4. Stored in MongoDB 'events' collection
    5. Used to build narrative and consequences
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    game_id: PyObjectId
    night: int
    event_type: str  # call, ambient, attack, discovery, ending
    title: str
    description: str
    triggered_by: Optional[str] = None  # caller_id or "system"
    consequences: Dict[str, Any] = Field(default_factory=dict)
    narrative_importance: int = 5  # 1-10 scale
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
