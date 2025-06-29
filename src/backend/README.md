# NBA Analytics FastAPI Backend

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up Environment Variables
Create a `.env` file:
```bash
DATABASE_URL=sqlite:///./nba_analytics.db
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### 3. Run the Application
```bash
# Development mode
uvicorn main:app --reload

# Production mode  
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 4. Access API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
src/backend/
├── app/
│   ├── api/routes/          # API endpoints
│   ├── core/               # Configuration
│   ├── db/                 # Database setup
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   └── services/           # Business logic
├── alembic/                # Database migrations
├── main.py                 # FastAPI application
└── requirements.txt        # Dependencies
```

## API Endpoints

### Players
- `GET /api/players` - List players with filtering
- `GET /api/players/{id}` - Get specific player
- `GET /api/players/{id}/stats` - Player statistics
- `GET /api/players/{id}/analytics` - Advanced analytics

### Teams  
- `GET /api/teams` - List teams
- `GET /api/teams/{id}` - Get specific team
- `GET /api/teams/{id}/players` - Team roster

### Analytics
- `GET /api/analytics/league-leaders` - Statistical leaders
- `GET /api/analytics/team-comparisons` - Compare teams
- `GET /api/analytics/player-efficiency` - Efficiency metrics

### Machine Learning
- `POST /api/ml/predict/game-outcome` - Game predictions
- `POST /api/ml/predict/player-performance` - Player predictions
- `GET /api/ml/models/status` - Model monitoring

## Development Focus

This backend is designed to practice:

✅ **FastAPI Development**: Modern Python web framework  
✅ **Database Design**: PostgreSQL with SQLAlchemy  
✅ **Data Engineering**: ETL pipelines and data processing  
✅ **Machine Learning**: Model deployment and serving  
✅ **API Design**: RESTful endpoints and documentation  
✅ **Performance**: Caching, optimization, monitoring  

## Next Steps

1. **Database Setup**: Configure PostgreSQL and run migrations
2. **Data Pipeline**: Implement NBA API data ingestion  
3. **Service Layer**: Complete business logic implementation
4. **Testing**: Add comprehensive test coverage
5. **ML Models**: Implement prediction algorithms
6. **Deployment**: Docker containerization and cloud deployment

Perfect for building ML engineering and backend development skills!
