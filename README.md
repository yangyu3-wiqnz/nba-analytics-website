# NBA Analytics API Platform

A backend-focused NBA data analytics platform for practicing data engineering, API development, and machine learning skills. Features a minimal frontend for testing and demonstration.

## 🎯 Project Focus

**Primary Goal**: Backend development and data analysis practice  
**Secondary Goal**: Simple frontend for API testing  
**Target Skills**: Data analysis → Machine Learning Engineering

## Project Structure

```
web_development/
├── docs/                          # 📚 Documentation and roadmaps
│   ├── NBA Website Development Roadmap.md  # Updated backend-focused roadmap
│   ├── NBA_API_Setup_Guide.md
│   └── src-folder-explained.md
├── src/                           # 💻 Source code
│   ├── frontend/                  # Simple testing interface
│   │   ├── pages/                # Basic HTML pages
│   │   │   ├── index.html        # Original demo (legacy)
│   │   │   └── api-test.html     # New API testing interface
│   │   └── assets/               # Static assets
│   │       ├── css/             # Simple Bootstrap styling
│   │       └── js/              # Vanilla JavaScript for API testing
│   └── backend/                  # Main focus - FastAPI development
│       ├── api/                 # REST API endpoints (future)
│       ├── models/              # SQLAlchemy models (future)
│       ├── utils/               # Data processing utilities (future)
│       └── ml/                  # Machine learning models (future)
├── scripts/                      # 🔧 Data processing and testing scripts
├── data/                         # 📊 Sample data and analysis
├── tests/                        # 🧪 API and backend testing
└── README.md                     # This file
```

## 🚀 Quick Start

### Current Testing Interface
1. Open `src/frontend/pages/api-test.html` in your browser
2. Test NBA APIs and explore data structure
3. Plan your FastAPI backend architecture

### Next Steps (Backend Development)
1. Set up FastAPI project structure
2. Design PostgreSQL database schema  
3. Build data ingestion pipelines
4. Create REST API endpoints
5. Implement ML models for predictions

## 🛠️ Technology Stack

### Backend (Primary Focus)
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Data Processing**: Pandas, NumPy, Scikit-learn
- **Caching**: Redis
- **Background Tasks**: Celery
- **Containerization**: Docker & Docker Compose

### Frontend (Minimal)
- **Framework**: Vanilla HTML/CSS/JavaScript
- **Styling**: Bootstrap 5 (no customization needed)
- **Charts**: Chart.js (simple data visualization)
- **Purpose**: API testing and basic data display only

### Data Sources
- **TheSportsDB**: Free NBA team and player data
- **balldontlie.io**: NBA-specific statistics API
- **Future**: Additional APIs for comprehensive data
## 🎯 Learning Objectives

### Backend Development Skills
- ✅ REST API design and implementation
- ✅ Database schema design and optimization
- ✅ Data pipeline architecture
- ✅ API authentication and security
- ✅ Performance optimization and caching
- ✅ API documentation and testing

### Data Analysis & ML Engineering
- ✅ Data ingestion from multiple sources
- ✅ Data cleaning and validation
- ✅ Statistical analysis and metrics calculation
- ✅ Machine learning model development
- ✅ Model deployment and monitoring
- ✅ Predictive analytics implementation

### DevOps & Deployment
- ✅ Docker containerization
- ✅ Database migration strategies
- ✅ Environment configuration management
- ✅ Monitoring and logging setup
- ✅ Performance testing and optimization

## � Development Phases

### Phase 1: Current (API Exploration)
- ✅ NBA API research and testing
- ✅ Simple frontend for API testing
- ✅ Data structure analysis
- ✅ Backend architecture planning

### Phase 2: Backend Foundation (Next)
- 🔲 FastAPI project setup
- 🔲 PostgreSQL database design
- 🔲 Data ingestion pipelines
- 🔲 Core API endpoints
- 🔲 Authentication system

### Phase 3: Advanced Analytics
- 🔲 Advanced statistical calculations
- 🔲 Data visualization endpoints
- 🔲 Performance optimization
- 🔲 Caching strategies

### Phase 4: Machine Learning
- 🔲 Predictive models development
- 🔲 Model deployment infrastructure
- 🔲 Real-time predictions API
- 🔲 Model monitoring and retraining

## 🔧 Current Features

### API Testing Interface
- Interactive testing of NBA APIs
- Response visualization and analysis
- Data structure exploration
- Basic charting capabilities
- Endpoint testing tools

### Sample Data Analysis
- NBA teams and players data export
- Statistical analysis examples
- Data quality assessment
- API response comparison

## 🚀 Getting Started

### 1. Explore Current Interface
```bash
# Open the API testing interface
open src/frontend/pages/api-test.html
```

### 2. Test NBA APIs
- Use the testing interface to explore TheSportsDB API
- Analyze data structures and response formats
- Plan your backend data models

### 3. Plan Backend Architecture
- Review the updated roadmap in `docs/`
- Design your database schema
- Plan API endpoint structure

## 📚 Documentation

- **[Updated Roadmap](docs/NBA%20Website%20Development%20Roadmap.md)**: Backend-focused development plan
- **[API Setup Guide](docs/NBA_API_Setup_Guide.md)**: NBA API integration guide
- **[Src Folder Guide](docs/src-folder-explained.md)**: Project structure explanation

## 🎓 Skills Development Focus

This project is designed to help you transition from **data analysis** to **machine learning engineering** by focusing on:

1. **Backend API Development** (70% of effort)
2. **Database Design & Optimization** (20% of effort)  
3. **Simple Frontend for Testing** (10% of effort)

The minimal frontend approach allows you to concentrate on building robust, scalable backend systems while still having a way to test and demonstrate your APIs.

## 🔄 Next Steps

1. **Set up FastAPI development environment**
2. **Design PostgreSQL database schema for NBA data**
3. **Build data ingestion pipelines from multiple APIs**
4. **Create comprehensive REST API endpoints**
5. **Implement machine learning models for predictions**
6. **Add comprehensive testing and documentation**

---

**Focus**: Building production-ready backend systems and data analysis skills for ML engineering career development.


## 📊 Data Sources

- **Primary**: balldontlie.io (Free NBA API)
- **Secondary**: TheSportsDB (Team details and metadata)
- **Strategy**: Hybrid approach - database for popular data, API for historical/rare queries

## 🏗️ Project Structure

```
nba-analytics-website/
├── backend/                 # FastAPI backend
│   ├── app/
│   ├── models/
│   ├── api/
│   └── requirements.txt
├── frontend/               # React frontend  
│   ├── src/
│   ├── public/
│   └── package.json
├── database/              # Database schemas and migrations
├── docker/               # Docker configuration
├── docs/                 # Documentation
└── tests/               # Test suites
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Docker (optional but recommended)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yangyu3-wiqnz/nba-analytics-website.git
   cd nba-analytics-website
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. **Database Setup**
   ```bash
   # Configure PostgreSQL connection in .env
   # Run migrations
   alembic upgrade head
   ```

## 📋 Development Roadmap

- [x] **Phase 1**: Planning & Discovery (1-2 weeks)
- [ ] **Phase 2**: Backend Development (3-4 weeks)
- [ ] **Phase 2.5**: Data Analytics Layer (1-2 weeks)
- [ ] **Phase 3**: Frontend Development (4-6 weeks)
- [ ] **Phase 4**: Testing & Deployment (1-2 weeks)
- [ ] **Phase 5**: Post-Launch & Iteration (Ongoing)

## 🤝 Contributing

This is a personal learning project, but feedback and suggestions are welcome! Please feel free to:
- Open issues for bugs or feature requests
- Submit pull requests for improvements
- Share ideas for analytics features

## 📈 Performance Strategy

### Database Design
- **Smart Caching**: Store frequently accessed data (current season, popular players)
- **Hybrid Approach**: Database for fast queries + API for comprehensive historical data
- **Efficient Size**: Targeting 100MB-1GB for core functionality
- **Data Freshness**: Automatic timestamp tracking and refresh rules

### User Experience
- **95% of queries**: Lightning-fast response from database cache
- **5% of queries**: Slightly slower but complete data from API
- **Progressive Enhancement**: Basic features work, advanced features enhance

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

Created by [Your Name] - Feel free to reach out!

---

⭐ **Star this repo if you find it helpful!**
