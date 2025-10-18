"""Call/transmission models."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from bson import ObjectId

from src.models.game import PyObjectId


class ConversationMessage(BaseModel):
    """
    Single message in a conversation.

    START HERE:
    1. Part of a call's conversation history
    2. Tracks who said what and when
    3. Can include emotional tone for AI context
    """

    speaker: str  # "caller" or "player"
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    emotion: Optional[str] = None  # terrified, calm, desperate, hopeful


class CallModel(BaseModel):
    """
    Individual radio transmission/call model.

    START HERE:
    1. Represents one complete call interaction
    2. Stores full conversation, choices made, outcomes
    3. Stored in MongoDB 'calls' collection
    4. Used by LlamaIndex to build caller memory
    5. Affects resource changes and trust scores
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    game_id: PyObjectId
    caller_id: str
    night: int
    time: str = "00:00 AM"  # In-game time
    duration: int = 0  # seconds
    conversation: List[ConversationMessage] = Field(default_factory=list)
    player_choices: List[int] = Field(default_factory=list)  # Menu options chosen
    outcome: Optional[str] = None  # helped, ignored, betrayed, doomed
    fuel_cost: float = 0.0
    sanity_impact: float = 0.0
    trust_impact: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
