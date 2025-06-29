// Player Card Component
class PlayerCard {
    constructor(playerData) {
        this.player = playerData;
    }

    render() {
        return `
            <div class="card player-card" data-player-id="${this.player.id}">
                <div class="player-header">
                    <img src="${this.player.photo || '/assets/images/player-placeholder.png'}" 
                         alt="${this.player.name}" 
                         class="player-photo">
                    <div class="player-info">
                        <h3 class="player-name">${this.player.name}</h3>
                        <p class="player-team">${this.player.team}</p>
                        <p class="player-position">${this.player.position}</p>
                    </div>
                </div>
                <div class="player-stats">
                    <div class="stat-item">
                        <span class="stat-label">PPG</span>
                        <span class="stat-value">${this.player.ppg || 'N/A'}</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">RPG</span>
                        <span class="stat-value">${this.player.rpg || 'N/A'}</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">APG</span>
                        <span class="stat-value">${this.player.apg || 'N/A'}</span>
                    </div>
                </div>
                <div class="player-actions">
                    <button class="btn btn-sm btn-primary" onclick="app.viewPlayer(${this.player.id})">
                        View Details
                    </button>
                    <button class="btn btn-sm btn-secondary" onclick="app.comparePlayer(${this.player.id})">
                        Compare
                    </button>
                </div>
            </div>
        `;
    }
}

// Team Card Component
class TeamCard {
    constructor(teamData) {
        this.team = teamData;
    }

    render() {
        return `
            <div class="card team-card" data-team-id="${this.team.id}">
                <div class="team-header">
                    <img src="${this.team.logo || '/assets/images/team-placeholder.png'}" 
                         alt="${this.team.name} logo" 
                         class="team-logo">
                    <div class="team-info">
                        <h3 class="team-name">${this.team.name}</h3>
                        <p class="team-city">${this.team.city}</p>
                        <p class="team-conference">${this.team.conference} Conference</p>
                    </div>
                </div>
                <div class="team-record">
                    <div class="record-item">
                        <span class="record-label">Wins</span>
                        <span class="record-value">${this.team.wins || 0}</span>
                    </div>
                    <div class="record-item">
                        <span class="record-label">Losses</span>
                        <span class="record-value">${this.team.losses || 0}</span>
                    </div>
                    <div class="record-item">
                        <span class="record-label">Win %</span>
                        <span class="record-value">${this.calculateWinPercentage()}%</span>
                    </div>
                </div>
                <div class="team-actions">
                    <button class="btn btn-sm btn-primary" onclick="app.viewTeam(${this.team.id})">
                        View Team
                    </button>
                    <button class="btn btn-sm btn-secondary" onclick="app.viewRoster(${this.team.id})">
                        Roster
                    </button>
                </div>
            </div>
        `;
    }

    calculateWinPercentage() {
        const wins = this.team.wins || 0;
        const losses = this.team.losses || 0;
        const total = wins + losses;
        return total > 0 ? ((wins / total) * 100).toFixed(1) : '0.0';
    }
}

// Game Card Component
class GameCard {
    constructor(gameData) {
        this.game = gameData;
    }

    render() {
        return `
            <div class="card game-card" data-game-id="${this.game.id}">
                <div class="game-header">
                    <div class="game-date">${this.formatDate(this.game.date)}</div>
                    <div class="game-status ${this.game.status.toLowerCase()}">${this.game.status}</div>
                </div>
                <div class="game-matchup">
                    <div class="team home-team">
                        <img src="${this.game.homeTeam.logo}" alt="${this.game.homeTeam.name}" class="team-logo-sm">
                        <span class="team-name">${this.game.homeTeam.name}</span>
                        <span class="team-score">${this.game.homeScore || ''}</span>
                    </div>
                    <div class="vs">VS</div>
                    <div class="team away-team">
                        <img src="${this.game.awayTeam.logo}" alt="${this.game.awayTeam.name}" class="team-logo-sm">
                        <span class="team-name">${this.game.awayTeam.name}</span>
                        <span class="team-score">${this.game.awayScore || ''}</span>
                    </div>
                </div>
                <div class="game-actions">
                    <button class="btn btn-sm btn-primary" onclick="app.viewGame(${this.game.id})">
                        ${this.game.status === 'Completed' ? 'Box Score' : 'Preview'}
                    </button>
                </div>
            </div>
        `;
    }

    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', { 
            month: 'short', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    }
}

// Stats Table Component
class StatsTable {
    constructor(data, columns) {
        this.data = data;
        this.columns = columns;
    }

    render() {
        return `
            <div class="stats-table-container">
                <table class="stats-table">
                    <thead>
                        <tr>
                            ${this.columns.map(col => `
                                <th class="sortable" data-column="${col.key}">
                                    ${col.label}
                                    <span class="sort-indicator"></span>
                                </th>
                            `).join('')}
                        </tr>
                    </thead>
                    <tbody>
                        ${this.data.map(row => `
                            <tr>
                                ${this.columns.map(col => `
                                    <td>${this.formatCellValue(row[col.key], col.type)}</td>
                                `).join('')}
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
    }

    formatCellValue(value, type) {
        if (value === null || value === undefined) return 'N/A';
        
        switch (type) {
            case 'percentage':
                return `${(value * 100).toFixed(1)}%`;
            case 'decimal':
                return value.toFixed(1);
            case 'integer':
                return Math.round(value);
            default:
                return value;
        }
    }
}

// Export components
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { PlayerCard, TeamCard, GameCard, StatsTable };
}
