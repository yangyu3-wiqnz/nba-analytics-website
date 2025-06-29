# Quick Reference: What Each File/Folder Does

## 🎯 **Frontend Files You'll Work With Most**

### **Pages** (`src/frontend/pages/`)
- `index.html` → **Homepage** - Main landing page with NBA dashboard
- Future: `teams.html`, `players.html`, `games.html`

### **Components** (`src/frontend/components/`)
- `Components.js` → **Reusable UI pieces**
  - `PlayerCard` class → Shows player photo, name, team, stats
  - `TeamCard` class → Shows team info, logo, record
  - `GameCard` class → Shows game scores, date, teams
  - `StatsChart` class → Creates interactive charts

### **Styles** (`src/frontend/assets/css/`)
- `main.css` → **Global styling**
  - NBA brand colors (blue #1d428a, red #c8102e)
  - Typography and layout
  - Button and card styles
  - Responsive design

### **JavaScript** (`src/frontend/assets/js/`)
- `main.js` → **Core functionality**
  - Page navigation
  - Component rendering
  - Event handling
  - User interactions

---

## ⚙️ **Backend Files (Future Development)**

### **API Routes** (`src/backend/api/`)
- `teams.js` → Handle requests like:
  - `GET /api/teams` → Get all teams
  - `GET /api/teams/lakers` → Get Lakers data
  
- `players.js` → Handle requests like:
  - `GET /api/players` → Get all players
  - `GET /api/players/lebron` → Get LeBron's stats

### **Data Models** (`src/backend/models/`)
- `Team.js` → Team structure: name, city, players, stats
- `Player.js` → Player structure: name, position, team, stats
- `Game.js` → Game structure: teams, score, date, venue

### **Utilities** (`src/backend/utils/`)
- `apiClient.js` → Fetch data from NBA APIs
- `dataProcessor.js` → Clean and organize API data
- `calculator.js` → Calculate averages, percentages, etc.

---

## 🔄 **How They Connect**

```
User visits website
       ↓
index.html loads
       ↓
main.css styles the page
       ↓
main.js makes the page interactive
       ↓
Components.js creates player/team cards
       ↓
API calls fetch NBA data
       ↓
Backend processes and returns data
       ↓
Frontend displays the data
```

---

## 💡 **Real Example**

**Scenario**: User wants to see Lakers team info

1. **User clicks "Teams"** → `index.html` navigation
2. **JavaScript handles click** → `main.js` 
3. **Fetches Lakers data** → `apiClient.js` calls TheSportsDB
4. **Creates team display** → `TeamCard` component
5. **Styles the display** → `main.css` team card styles
6. **Shows to user** → Beautiful Lakers team card with logo, roster, stats

---

## 🛠️ **What You'll Actually Build**

1. **Start with**: HTML pages showing static NBA content
2. **Add styling**: Make it look professional with CSS
3. **Add interactivity**: JavaScript for clicks, navigation
4. **Connect to data**: Use your export scripts to show real NBA data
5. **Add backend**: API endpoints to serve data efficiently

Each folder has a specific job, making your code organized and easy to maintain!
