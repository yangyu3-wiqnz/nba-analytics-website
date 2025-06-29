"""
NBA Analytics FastAPI Application

A backend API for NBA data analysis, statistics, and machine learning predictions.
Focus: Backend development, database optimization, and ML engineering practice.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
import logging

from app.core.config import settings
from app.api.routes import players, teams, analytics, ml_models
from app.db.database import engine
from app.models import Base

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="NBA Analytics API",
    description="""
    🏀 **NBA Analytics Backend API**
    
    A comprehensive backend platform for NBA data analysis and machine learning.
    
    ## Features
    
    * **Player Analytics**: Advanced player statistics and performance metrics
    * **Team Analytics**: Team performance analysis and comparisons  
    * **Machine Learning**: Predictive models for game outcomes and player performance
    * **Data Pipeline**: Real-time data ingestion from multiple NBA APIs
    * **Advanced Statistics**: Calculate custom NBA metrics and analytics
    
    ## Focus Areas
    
    * Backend API development with FastAPI
    * Database design and optimization (PostgreSQL)
    * Data engineering and pipeline development
    * Machine learning model deployment and serving
    * Performance optimization and caching strategies
    
    **Perfect for**: Data analysts transitioning to ML engineering roles
    """,
    version="1.0.0",
    contact={
        "name": "NBA Analytics Platform",
        "url": "https://github.com/yourusername/nba-analytics",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add timing middleware for performance monitoring
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Include API routes
app.include_router(players.router, prefix="/api/players", tags=["Players"])
app.include_router(teams.router, prefix="/api/teams", tags=["Teams"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(ml_models.router, prefix="/api/ml", tags=["Machine Learning"])

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """
    Welcome endpoint for the NBA Analytics API.
    
    Returns basic information about the API and available endpoints.
    """
    return {
        "message": "🏀 NBA Analytics API",
        "description": "Backend platform for NBA data analysis and machine learning",
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "endpoints": {
            "players": "/api/players",
            "teams": "/api/teams", 
            "analytics": "/api/analytics",
            "machine_learning": "/api/ml"
        },
        "focus": "Backend development, database optimization, ML engineering"
    }

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint for monitoring and deployment.
    """
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0"
    }

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred. Please try again later.",
            "path": str(request.url)
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
