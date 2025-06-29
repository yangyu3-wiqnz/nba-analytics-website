// NBA Analytics App - Main JavaScript
class NBAApp {
    constructor() {
        this.apiEndpoints = {
            teams: '/api/teams',
            players: '/api/players',
            games: '/api/games',
            stats: '/api/stats'
        };
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadInitialData();
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', this.handleNavigation.bind(this));
        });

        // Search functionality
        const searchInput = document.getElementById('player-search');
        if (searchInput) {
            searchInput.addEventListener('input', this.debounce(this.handleSearch.bind(this), 300));
        }

        // Filter controls
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', this.handleFilter.bind(this));
        });
    }

    async loadInitialData() {
        try {
            // Load teams data
            const teams = await this.fetchData(this.apiEndpoints.teams);
            this.renderTeams(teams);

            // Load featured players
            const players = await this.fetchData(`${this.apiEndpoints.players}?featured=true`);
            this.renderFeaturedPlayers(players);

        } catch (error) {
            console.error('Error loading initial data:', error);
            this.showError('Failed to load NBA data. Please try again later.');
        }
    }

    async fetchData(url) {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    }

    renderTeams(teams) {
        const container = document.getElementById('teams-container');
        if (!container) return;

        container.innerHTML = teams.map(team => `
            <div class="card team-card" data-team-id="${team.id}">
                <img src="${team.logo}" alt="${team.name} logo" class="team-logo">
                <h3>${team.name}</h3>
                <p class="team-record">${team.wins}-${team.losses}</p>
                <button class="btn btn-sm" onclick="app.viewTeam(${team.id})">
                    View Team
                </button>
            </div>
        `).join('');
    }

    renderFeaturedPlayers(players) {
        const container = document.getElementById('players-container');
        if (!container) return;

        container.innerHTML = players.map(player => `
            <div class="card player-card" data-player-id="${player.id}">
                <img src="${player.photo}" alt="${player.name}" class="player-photo">
                <h3>${player.name}</h3>
                <p class="player-team">${player.team}</p>
                <p class="player-position">${player.position}</p>
                <div class="player-stats">
                    <span>PPG: ${player.ppg}</span>
                    <span>RPG: ${player.rpg}</span>
                    <span>APG: ${player.apg}</span>
                </div>
                <button class="btn btn-sm" onclick="app.viewPlayer(${player.id})">
                    View Player
                </button>
            </div>
        `).join('');
    }

    handleNavigation(event) {
        event.preventDefault();
        const page = event.target.dataset.page;
        this.loadPage(page);
    }

    handleSearch(event) {
        const query = event.target.value.trim();
        if (query.length >= 2) {
            this.searchPlayers(query);
        }
    }

    handleFilter(event) {
        const filterType = event.target.dataset.filter;
        const filterValue = event.target.dataset.value;
        this.applyFilter(filterType, filterValue);
    }

    async searchPlayers(query) {
        try {
            const players = await this.fetchData(`${this.apiEndpoints.players}?search=${encodeURIComponent(query)}`);
            this.renderSearchResults(players);
        } catch (error) {
            console.error('Search error:', error);
        }
    }

    applyFilter(type, value) {
        // Update active filter UI
        document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');

        // Apply filter logic
        const items = document.querySelectorAll(`.${type}-item`);
        items.forEach(item => {
            const shouldShow = value === 'all' || item.dataset[type] === value;
            item.style.display = shouldShow ? 'block' : 'none';
        });
    }

    viewTeam(teamId) {
        // Navigate to team page
        window.location.href = `/team/${teamId}`;
    }

    viewPlayer(playerId) {
        // Navigate to player page
        window.location.href = `/player/${playerId}`;
    }

    showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        document.body.appendChild(errorDiv);

        setTimeout(() => {
            errorDiv.remove();
        }, 5000);
    }

    // Utility function to debounce search input
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.app = new NBAApp();
});

// Chart utilities for data visualization
class ChartUtils {
    static createPlayerStatsChart(containerId, playerData) {
        // Implementation for player stats chart
        // Using Chart.js or similar library
    }

    static createTeamComparisonChart(containerId, teamData) {
        // Implementation for team comparison chart
    }

    static createSeasonTrendsChart(containerId, seasonData) {
        // Implementation for season trends chart
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { NBAApp, ChartUtils };
}
