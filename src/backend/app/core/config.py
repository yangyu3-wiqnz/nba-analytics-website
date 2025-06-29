"""
Configuration settings for NBA Analytics API

Handles environment variables, database settings, and application configuration.
"""

from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    
    # Application settings
    APP_NAME: str = "NBA Analytics API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS settings
    ALLOWED_HOSTS: List[str] = ["http://localhost:3000", "http://localhost:8080", "*"]
    
    # Database settings
    DATABASE_URL: str = "postgresql://username:password@localhost:5432/nba_analytics"
    DATABASE_ECHO: bool = False  # Set to True for SQL query logging
    
    # Redis settings
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_TTL: int = 3600  # Cache time-to-live in seconds
    
    # External NBA APIs
    THESPORTSDB_BASE_URL: str = "https://www.thesportsdb.com/api/v1/json/3"
    BALLDONTLIE_BASE_URL: str = "https://www.balldontlie.io/api/v1"
    
    # API Rate limiting
    REQUESTS_PER_MINUTE: int = 60
    
    # Machine Learning settings
    ML_MODEL_PATH: str = "models/"
    MODEL_RETRAIN_INTERVAL: int = 86400  # 24 hours in seconds
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Security settings
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Data processing
    BATCH_SIZE: int = 1000
    MAX_WORKERS: int = 4
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()


# Database configuration helper
def get_database_url() -> str:
    """
    Get database URL with fallback for development.
    """
    if settings.DATABASE_URL.startswith("postgresql://username:password"):
        # Development fallback - using SQLite for easy setup
        return "sqlite:///./nba_analytics.db"
    return settings.DATABASE_URL


# Logging configuration
def setup_logging():
    """
    Configure application logging.
    """
    import logging
    
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL),
        format=settings.LOG_FORMAT,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("app.log")
        ]
    )
    
    # Reduce noise from third-party libraries
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


# Environment detection
def is_development() -> bool:
    """Check if running in development mode."""
    return settings.DEBUG


def is_production() -> bool:
    """Check if running in production mode."""
    return not settings.DEBUG
