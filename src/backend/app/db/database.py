"""
Database configuration and session management for NBA Analytics API.

Handles SQLAlchemy engine, session management, and database connection.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
import logging

from app.core.config import get_database_url, settings

logger = logging.getLogger(__name__)

# Database URL
DATABASE_URL = get_database_url()

# Create SQLAlchemy engine
# For SQLite (development), we need check_same_thread=False
# For PostgreSQL (production), this parameter is ignored
engine = create_engine(
    DATABASE_URL,
    echo=settings.DATABASE_ECHO,  # Set to True to see SQL queries
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for declarative models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Database session dependency for FastAPI.
    
    Yields a database session and ensures it's closed after use.
    Use this in your API endpoints with Depends(get_db).
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def create_tables():
    """
    Create all database tables.
    
    This will create tables based on your SQLAlchemy models.
    """
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise


def drop_tables():
    """
    Drop all database tables.
    
    WARNING: This will delete all data! Use only in development.
    """
    if settings.DEBUG:
        Base.metadata.drop_all(bind=engine)
        logger.warning("All database tables dropped")
    else:
        logger.error("Cannot drop tables in production mode")


# Database health check
def check_database_connection() -> bool:
    """
    Check if database connection is working.
    
    Returns True if connection is successful, False otherwise.
    """
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        logger.info("Database connection successful")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False


# Initialize database on import
def init_db():
    """
    Initialize database with tables and basic setup.
    """
    logger.info(f"Initializing database with URL: {DATABASE_URL}")
    
    # Check connection
    if not check_database_connection():
        raise Exception("Cannot connect to database")
    
    # Create tables
    create_tables()
    
    logger.info("Database initialization completed")
