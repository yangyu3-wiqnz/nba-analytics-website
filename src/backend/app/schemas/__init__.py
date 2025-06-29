"""
Pydantic schemas for NBA Analytics API.

Define data models for API requests and responses with automatic validation.
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


# Enums for better type safety
class Position(str, Enum):
    POINT_GUARD = "PG"
    SHOOTING_GUARD = "SG" 
    SMALL_FORWARD = "SF"
    POWER_FORWARD = "PF"
    CENTER = "C"


class Conference(str, Enum):
    EASTERN = "Eastern"
    WESTERN = "Western"


class GameStatus(str, Enum):
    SCHEDULED = "scheduled"
    LIVE = "live"
    COMPLETED = "completed"


# Base schemas
class TeamBase(BaseModel):
    """Base schema for team data."""
    name: str = Field(..., min_length=1, max_length=100)
    city: str = Field(..., min_length=1, max_length=50)
    abbreviation: str = Field(..., min_length=2, max_length=3)
    conference: Optional[Conference] = None
    division: Optional[str] = None
    founded_year: Optional[int] = Field(None, ge=1946, le=2025)


class TeamCreate(TeamBase):
    """Schema for creating a new team."""
    external_id: Optional[str] = None


class TeamUpdate(BaseModel):
    """Schema for updating team data."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    city: Optional[str] = Field(None, min_length=1, max_length=50)
    conference: Optional[Conference] = None
    division: Optional[str] = None
    is_active: Optional[bool] = None


class Team(TeamBase):
    """Schema for team response data."""
    id: int
    external_id: Optional[str] = None
    is_active: bool = True
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# Player schemas
class PlayerBase(BaseModel):
    """Base schema for player data."""
    name: str = Field(..., min_length=1, max_length=100)
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    position: Optional[Position] = None
    height: Optional[str] = Field(None, max_length=10)
    weight: Optional[str] = Field(None, max_length=10)
    birth_date: Optional[datetime] = None
    birth_place: Optional[str] = Field(None, max_length=100)
    jersey_number: Optional[int] = Field(None, ge=0, le=99)
    years_pro: Optional[int] = Field(None, ge=0, le=30)
    college: Optional[str] = Field(None, max_length=100)


class PlayerCreate(PlayerBase):
    """Schema for creating a new player."""
    external_id: Optional[str] = None
    team_id: Optional[int] = None


class PlayerUpdate(BaseModel):
    """Schema for updating player data."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    position: Optional[Position] = None
    team_id: Optional[int] = None
    jersey_number: Optional[int] = Field(None, ge=0, le=99)
    is_active: Optional[bool] = None
    is_rookie: Optional[bool] = None


class Player(PlayerBase):
    """Schema for player response data."""
    id: int
    external_id: Optional[str] = None
    team_id: Optional[int] = None
    is_active: bool = True
    is_rookie: bool = False
    created_at: datetime
    updated_at: Optional[datetime] = None
    team: Optional[Team] = None
    
    class Config:
        from_attributes = True


# Game schemas
class GameBase(BaseModel):
    """Base schema for game data."""
    season: str = Field(..., min_length=7, max_length=7)  # e.g., "2023-24"
    game_date: datetime
    home_team_id: int
    away_team_id: int
    home_score: Optional[int] = Field(None, ge=0)
    away_score: Optional[int] = Field(None, ge=0)
    status: GameStatus = GameStatus.SCHEDULED
    quarter: Optional[int] = Field(None, ge=1, le=4)
    time_remaining: Optional[str] = None
    game_type: str = "regular"


class GameCreate(GameBase):
    """Schema for creating a new game."""
    external_id: Optional[str] = None


class GameUpdate(BaseModel):
    """Schema for updating game data."""
    home_score: Optional[int] = Field(None, ge=0)
    away_score: Optional[int] = Field(None, ge=0)
    status: Optional[GameStatus] = None
    quarter: Optional[int] = Field(None, ge=1, le=4)
    time_remaining: Optional[str] = None


class Game(GameBase):
    """Schema for game response data."""
    id: int
    external_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    home_team: Optional[Team] = None
    away_team: Optional[Team] = None
    
    class Config:
        from_attributes = True


# Player statistics schemas
class PlayerStatsBase(BaseModel):
    """Base schema for player statistics."""
    minutes_played: Optional[float] = Field(None, ge=0, le=48)
    points: int = Field(0, ge=0)
    rebounds: int = Field(0, ge=0)
    assists: int = Field(0, ge=0)
    steals: int = Field(0, ge=0)
    blocks: int = Field(0, ge=0)
    turnovers: int = Field(0, ge=0)
    fouls: int = Field(0, ge=0)
    field_goals_made: int = Field(0, ge=0)
    field_goals_attempted: int = Field(0, ge=0)
    three_pointers_made: int = Field(0, ge=0)
    three_pointers_attempted: int = Field(0, ge=0)
    free_throws_made: int = Field(0, ge=0)
    free_throws_attempted: int = Field(0, ge=0)
    plus_minus: Optional[int] = None


class PlayerStatsCreate(PlayerStatsBase):
    """Schema for creating player statistics."""
    player_id: int
    game_id: int


class PlayerStats(PlayerStatsBase):
    """Schema for player statistics response."""
    id: int
    player_id: int
    game_id: int
    field_goal_percentage: Optional[float] = None
    three_point_percentage: Optional[float] = None
    free_throw_percentage: Optional[float] = None
    created_at: datetime
    player: Optional[Player] = None
    game: Optional[Game] = None
    
    class Config:
        from_attributes = True


# Analytics schemas
class PlayerAnalytics(BaseModel):
    """Schema for player analytics data."""
    player_id: int
    player_name: str
    games_played: int
    avg_points: float
    avg_rebounds: float
    avg_assists: float
    avg_minutes: float
    field_goal_percentage: float
    three_point_percentage: float
    free_throw_percentage: float
    efficiency_rating: Optional[float] = None


class TeamAnalytics(BaseModel):
    """Schema for team analytics data."""
    team_id: int
    team_name: str
    games_played: int
    wins: int
    losses: int
    win_percentage: float
    avg_points_scored: float
    avg_points_allowed: float
    avg_rebounds: float
    avg_assists: float


# Search and filter schemas
class PlayerSearch(BaseModel):
    """Schema for player search parameters."""
    name: Optional[str] = None
    team_id: Optional[int] = None
    position: Optional[Position] = None
    is_active: Optional[bool] = True
    limit: int = Field(50, ge=1, le=100)
    offset: int = Field(0, ge=0)


class GameSearch(BaseModel):
    """Schema for game search parameters."""
    season: Optional[str] = None
    team_id: Optional[int] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    status: Optional[GameStatus] = None
    limit: int = Field(50, ge=1, le=100)
    offset: int = Field(0, ge=0)


# Response schemas
class APIResponse(BaseModel):
    """Generic API response schema."""
    success: bool = True
    message: str = "Operation successful"
    data: Optional[dict] = None


class PaginatedResponse(BaseModel):
    """Schema for paginated responses."""
    items: List[dict]
    total: int
    limit: int
    offset: int
    has_next: bool
    has_previous: bool


# Machine Learning schemas
class PredictionRequest(BaseModel):
    """Schema for ML prediction requests."""
    home_team_id: int
    away_team_id: int
    game_date: Optional[datetime] = None


class PredictionResponse(BaseModel):
    """Schema for ML prediction responses."""
    home_team_win_probability: float = Field(..., ge=0, le=1)
    away_team_win_probability: float = Field(..., ge=0, le=1)
    predicted_score_home: Optional[int] = None
    predicted_score_away: Optional[int] = None
    confidence: float = Field(..., ge=0, le=1)
    model_version: str
    features_used: List[str]
    
    @validator('away_team_win_probability')
    def probabilities_sum_to_one(cls, v, values):
        if 'home_team_win_probability' in values:
            total = v + values['home_team_win_probability']
            if not (0.99 <= total <= 1.01):  # Allow small floating point errors
                raise ValueError('Win probabilities must sum to 1.0')
        return v
