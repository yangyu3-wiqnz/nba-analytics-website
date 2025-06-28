# 🏀 NBA Analytics Website

A comprehensive NBA analytics website built with modern web technologies, designed for both casual basketball fans and data analysts.

## 🎯 Project Overview

This project combines real-time NBA data with advanced analytics to create an interactive platform for exploring basketball statistics, player comparisons, and team performance metrics.

## 🚀 Features

### Core Features
- **Advanced Player Search** - Filter by position, team, statistics
- **Detailed Player Profiles** - Stats, bio, photos, career highlights  
- **Team Pages** - Rosters and comprehensive team statistics
- **Live Scores & Schedules** - Real-time game information
- **Interactive Visualizations** - Charts and graphs for data analysis
- **Player Comparison Tools** - Side-by-side statistical analysis

### Target Audiences
- **Casual Fans**: Easy-to-use interface with visual stats and engaging content
- **Data Analysts**: Advanced metrics, data export capabilities, and detailed statistics

## 🛠️ Technology Stack

- **Backend**: Python with FastAPI
- **Frontend**: React with TypeScript
- **Database**: PostgreSQL
- **Caching**: Redis
- **Data Processing**: Pandas & SQLAlchemy
- **Containerization**: Docker & Docker Compose
- **Visualizations**: Plotly.js / Chart.js

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
