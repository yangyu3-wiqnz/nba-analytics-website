# Detailed Explanation of the `src` Folder Structure

The `src` (source) folder is the heart of your NBA analytics website application. It contains all the code that makes your website function. Here's a detailed breakdown:

## 📁 `src/` - Main Source Directory

This is where all your application code lives, separated into **frontend** (what users see) and **backend** (server logic).

---

## 🎨 `src/frontend/` - Client-Side Code

This contains everything that runs in the user's web browser.

### 📁 `src/frontend/pages/`
**Purpose**: Contains the main pages/screens of your website
**Examples**:
- `index.html` - Homepage with NBA dashboard
- `teams.html` - Team comparison page  
- `players.html` - Player statistics page
- `analytics.html` - Advanced analytics page

**What goes here**: Each major section or route of your website gets its own page file.

### 📁 `src/frontend/components/`
**Purpose**: Reusable UI pieces that can be used across multiple pages
**Examples**:
- `PlayerCard.js` - A card showing player stats
- `TeamLogo.js` - Component to display team logos
- `StatsChart.js` - Chart component for displaying statistics
- `NavigationBar.js` - Website navigation menu
- `GameSchedule.js` - Component showing upcoming games

**What goes here**: Small, reusable pieces of UI that you might use on multiple pages.

### 📁 `src/frontend/assets/` - Static Files

#### 📁 `src/frontend/assets/css/`
**Purpose**: All styling files
**Examples**:
- `main.css` - Global styles for the entire site
- `components.css` - Styles for reusable components
- `pages.css` - Page-specific styles
- `responsive.css` - Mobile/tablet responsive styles

#### 📁 `src/frontend/assets/js/`
**Purpose**: JavaScript functionality
**Examples**:
- `main.js` - Core website functionality
- `api.js` - Functions to fetch NBA data from APIs
- `charts.js` - Chart creation and manipulation
- `utils.js` - Helper functions (date formatting, calculations)

#### 📁 `src/frontend/assets/images/`
**Purpose**: All images and graphics
**Examples**:
- `logo.png` - Your website logo
- `team-logos/` - NBA team logos
- `player-photos/` - Player headshots
- `icons/` - UI icons (stats, navigation, etc.)

---

## ⚙️ `src/backend/` - Server-Side Code

This contains code that runs on your server to process data and handle requests.

### 📁 `src/backend/api/`
**Purpose**: API endpoints that frontend calls to get data
**Examples**:
- `teams.js` - Endpoints for team data (`/api/teams`, `/api/teams/:id`)
- `players.js` - Player-related endpoints (`/api/players`, `/api/players/search`)
- `games.js` - Game data endpoints (`/api/games/today`, `/api/games/schedule`)
- `stats.js` - Statistics endpoints (`/api/stats/team/:id`, `/api/stats/player/:id`)

**What goes here**: Functions that handle HTTP requests and return JSON data.

### 📁 `src/backend/models/`
**Purpose**: Data structures and database schemas
**Examples**:
- `Team.js` - Team data model (id, name, city, stats, etc.)
- `Player.js` - Player data model (id, name, position, stats, etc.)
- `Game.js` - Game data model (teams, score, date, etc.)
- `Stats.js` - Statistics data model (points, rebounds, assists, etc.)

**What goes here**: Definitions of how your data is structured and organized.

### 📁 `src/backend/utils/`
**Purpose**: Helper functions and utilities
**Examples**:
- `dataProcessor.js` - Functions to clean and process NBA API data
- `calculator.js` - Statistical calculations (averages, percentages, etc.)
- `apiClient.js` - Functions to call external NBA APIs
- `cache.js` - Data caching functionality
- `logger.js` - Logging and error tracking

**What goes here**: Reusable functions that support your main application logic.

---

## 🔄 How They Work Together

### Example Data Flow:
1. **User visits homepage** → `frontend/pages/index.html`
2. **Page needs team data** → `frontend/assets/js/api.js` calls `/api/teams`
3. **Backend receives request** → `backend/api/teams.js` handles the request
4. **Backend gets data** → Uses `backend/utils/apiClient.js` to fetch from NBA API
5. **Backend processes data** → `backend/models/Team.js` structures the data
6. **Frontend receives data** → `frontend/components/TeamCard.js` displays it
7. **User sees styled content** → `frontend/assets/css/main.css` styles everything

### Example File Interactions:
```
frontend/pages/teams.html
    ↓ (uses)
frontend/components/TeamCard.js
    ↓ (styled by)
frontend/assets/css/components.css
    ↓ (gets data via)
frontend/assets/js/api.js
    ↓ (calls)
backend/api/teams.js
    ↓ (uses)
backend/models/Team.js
    ↓ (fetches via)
backend/utils/apiClient.js
```

---

## 🛠️ Current State vs Future

### Currently Set Up:
- Basic folder structure
- Template README files
- Example component files

### What You'll Add:
- Actual HTML pages for NBA data
- CSS styles for your design
- JavaScript to fetch and display NBA statistics
- API endpoints to process NBA data
- Data models for teams, players, games

This structure gives you a solid foundation to build a professional NBA analytics website that can grow and scale as you add more features!
