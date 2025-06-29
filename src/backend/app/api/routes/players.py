"""
Player API routes for NBA Analytics.

Endpoints for player data, statistics, and analytics.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.schemas import Player, PlayerCreate, PlayerUpdate, PlayerSearch, PlayerAnalytics
from app.services.player_service import PlayerService

router = APIRouter()


@router.get("/", response_model=List[Player])
async def get_players(
    skip: int = Query(0, ge=0, description="Number of players to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of players to return"),
    team_id: Optional[int] = Query(None, description="Filter by team ID"),
    position: Optional[str] = Query(None, description="Filter by position (PG, SG, SF, PF, C)"),
    is_active: Optional[bool] = Query(True, description="Filter by active status"),
    db: Session = Depends(get_db)
):
    """
    Get list of NBA players with optional filtering.
    
    - **skip**: Number of players to skip (for pagination)
    - **limit**: Maximum number of players to return
    - **team_id**: Filter players by team
    - **position**: Filter by player position
    - **is_active**: Show only active players (default: True)
    """
    try:
        player_service = PlayerService(db)
        players = player_service.get_players(
            skip=skip,
            limit=limit,
            team_id=team_id,
            position=position,
            is_active=is_active
        )
        return players
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving players: {str(e)}")


@router.get("/search", response_model=List[Player])
async def search_players(
    name: Optional[str] = Query(None, description="Search by player name"),
    team_name: Optional[str] = Query(None, description="Search by team name"),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Search for players by name or team.
    
    - **name**: Search for players with names containing this string
    - **team_name**: Search for players on teams containing this string
    - **limit**: Maximum number of results to return
    """
    try:
        player_service = PlayerService(db)
        players = player_service.search_players(
            name=name,
            team_name=team_name,
            limit=limit
        )
        return players
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching players: {str(e)}")


@router.get("/{player_id}", response_model=Player)
async def get_player(player_id: int, db: Session = Depends(get_db)):
    """
    Get a specific player by ID.
    
    Returns detailed player information including team data.
    """
    try:
        player_service = PlayerService(db)
        player = player_service.get_player_by_id(player_id)
        
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        
        return player
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving player: {str(e)}")


@router.get("/{player_id}/stats")
async def get_player_stats(
    player_id: int,
    season: Optional[str] = Query(None, description="Filter by season (e.g., '2023-24')"),
    last_n_games: Optional[int] = Query(None, ge=1, le=82, description="Get stats for last N games"),
    db: Session = Depends(get_db)
):
    """
    Get statistics for a specific player.
    
    - **season**: Filter stats by season
    - **last_n_games**: Get stats for the most recent N games
    """
    try:
        player_service = PlayerService(db)
        
        # Check if player exists
        player = player_service.get_player_by_id(player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        
        stats = player_service.get_player_stats(
            player_id=player_id,
            season=season,
            last_n_games=last_n_games
        )
        
        return {
            "player_id": player_id,
            "player_name": player.name,
            "season": season,
            "total_games": len(stats),
            "statistics": stats
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving player stats: {str(e)}")


@router.get("/{player_id}/analytics", response_model=PlayerAnalytics)
async def get_player_analytics(
    player_id: int,
    season: Optional[str] = Query(None, description="Season for analytics (e.g., '2023-24')"),
    db: Session = Depends(get_db)
):
    """
    Get advanced analytics for a specific player.
    
    Returns calculated metrics like efficiency rating, averages, and percentages.
    """
    try:
        player_service = PlayerService(db)
        
        # Check if player exists
        player = player_service.get_player_by_id(player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        
        analytics = player_service.get_player_analytics(player_id, season)
        
        if not analytics:
            raise HTTPException(
                status_code=404, 
                detail=f"No analytics data found for player {player_id}"
            )
        
        return analytics
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating player analytics: {str(e)}")


@router.get("/{player_id}/similar")
async def get_similar_players(
    player_id: int,
    limit: int = Query(5, ge=1, le=20, description="Number of similar players to return"),
    season: Optional[str] = Query(None, description="Season to base similarity on"),
    db: Session = Depends(get_db)
):
    """
    Find players similar to the specified player.
    
    Uses statistical analysis to find players with similar performance profiles.
    This is a placeholder for future ML implementation.
    """
    try:
        player_service = PlayerService(db)
        
        # Check if player exists
        player = player_service.get_player_by_id(player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        
        # Placeholder for similarity algorithm
        similar_players = player_service.find_similar_players(
            player_id=player_id,
            limit=limit,
            season=season
        )
        
        return {
            "player_id": player_id,
            "player_name": player.name,
            "similar_players": similar_players,
            "algorithm": "statistical_similarity",
            "note": "This is a placeholder implementation. Advanced ML similarity will be added later."
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error finding similar players: {str(e)}")


@router.post("/", response_model=Player)
async def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    """
    Create a new player.
    
    Used for adding players from external APIs or manual entry.
    """
    try:
        player_service = PlayerService(db)
        
        # Check if player already exists by external_id or name
        if player.external_id:
            existing = player_service.get_player_by_external_id(player.external_id)
            if existing:
                raise HTTPException(
                    status_code=400, 
                    detail="Player with this external_id already exists"
                )
        
        new_player = player_service.create_player(player)
        return new_player
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating player: {str(e)}")


@router.put("/{player_id}", response_model=Player)
async def update_player(
    player_id: int, 
    player_update: PlayerUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update an existing player.
    
    Only updates fields that are provided in the request.
    """
    try:
        player_service = PlayerService(db)
        
        # Check if player exists
        existing_player = player_service.get_player_by_id(player_id)
        if not existing_player:
            raise HTTPException(status_code=404, detail="Player not found")
        
        updated_player = player_service.update_player(player_id, player_update)
        return updated_player
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating player: {str(e)}")


@router.delete("/{player_id}")
async def delete_player(player_id: int, db: Session = Depends(get_db)):
    """
    Delete a player (soft delete - marks as inactive).
    
    This doesn't actually delete the player from the database,
    but marks them as inactive to preserve historical data.
    """
    try:
        player_service = PlayerService(db)
        
        # Check if player exists
        player = player_service.get_player_by_id(player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        
        player_service.soft_delete_player(player_id)
        
        return {
            "message": f"Player {player.name} has been deactivated",
            "player_id": player_id
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting player: {str(e)}")
