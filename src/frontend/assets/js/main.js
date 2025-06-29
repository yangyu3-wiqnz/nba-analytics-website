/**
 * NBA Analytics Website - Main Application
 * Handles page navigation, data loading, and UI interactions
 */

class NBAApp {
    constructor() {
        this.api = new NBADataAPI();
        this.currentPage = 'home';
        this.init();
    }

    async init() {
        console.log('🏀 NBA Analytics App Starting...');
        
        try {
            // Set up navigation
            this.setupNavigation();
            
            // Set up card interactions
            this.setupInteractivity();
            
            // Load initial page content
            await this.loadHomePage();
            
            console.log('✅ App initialized successfully');
        } catch (error) {
            console.error('❌ App initialization failed:', error);
            this.showError('Failed to initialize app. Please refresh the page.');
        }
    }

    setupNavigation() {
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const page = e.target.dataset.page;
                this.navigateToPage(page);
            });
        });
    }

    async navigateToPage(page) {
        // Update active nav link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelector(`[data-page="${page}"]`)?.classList.add('active');

        // Load page content
        switch(page) {
            case 'home':
                await this.loadHomePage();
                break;
            case 'teams':
                await this.loadTeamsPage();
                break;
            case 'players':
                await this.loadPlayersPage();
                break;
            default:
                this.showComingSoon(page);
        }
    }

    async loadHomePage() {
        console.log('Loading homepage...');
        const mainContent = document.getElementById('main-content');
        
        // Show loading state
        mainContent.innerHTML = `
            <div class="loading-container">
                <div class="loading-spinner"></div>
                <p>Loading NBA data...</p>
            </div>
        `;

        try {
            // Fetch data in parallel
            const [teams, featuredPlayers] = await Promise.all([
                this.api.fetchTeams(),
                this.api.getFeaturedPlayers()
            ]);

            // Render homepage
            mainContent.innerHTML = this.renderHomePage(teams, featuredPlayers);
            
            console.log(`✅ Loaded ${teams.length} teams and ${featuredPlayers.length} featured players`);
        } catch (error) {
            console.error('Error loading homepage:', error);
            this.showError('Failed to load NBA data. Please try again.');
        }
    }

    renderHomePage(teams, featuredPlayers) {
        return `
            <div class="hero-section">
                <div class="container">
                    <h1 class="hero-title">NBA Analytics Hub</h1>
                    <p class="hero-subtitle">Your ultimate destination for NBA statistics, team insights, and player analytics</p>
                    <div class="hero-stats">
                        <div class="stat-card">
                            <div class="stat-number">${teams.length}</div>
                            <div class="stat-label">NBA Teams</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number">${featuredPlayers.length}</div>
                            <div class="stat-label">Featured Players</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number">Live</div>
                            <div class="stat-label">Data Updates</div>
                        </div>
                    </div>
                </div>
            </div>

            <section class="featured-teams">
                <div class="container">
                    <h2 class="section-title">NBA Teams</h2>
                    <div class="teams-grid">
                        ${(() => {
                            const displayTeams = teams.slice(0, 8);
                            console.log(`Rendering ${displayTeams.length} teams out of ${teams.length} total teams`);
                            return displayTeams.map(team => this.renderTeamCard(team)).join('');
                        })()}
                    </div>
                    <div class="section-footer">
                        <button class="btn btn-secondary" onclick="app.navigateToPage('teams')">View All Teams</button>
                    </div>
                </div>
            </section>

            <section class="featured-players">
                <div class="container">
                    <h2 class="section-title">Featured Players</h2>
                    <div class="players-grid">
                        ${featuredPlayers.map(player => this.renderPlayerCard(player)).join('')}
                    </div>
                    <div class="section-footer">
                        <button class="btn btn-secondary" onclick="app.navigateToPage('players')">View All Players</button>
                    </div>
                </div>
            </section>
        `;
    }

    renderTeamCard(team) {
        const teamName = team.strTeam || 'Unknown Team';
        // Create better initials - take first letter of each word, max 3 letters
        const teamInitials = teamName.split(' ')
            .map(word => word[0])
            .join('')
            .substring(0, 3)
            .toUpperCase();
        
        return `
            <div class="card team-card" data-team-id="${team.idTeam}" title="Click to view ${teamName} details">
                <div class="team-logo">
                    <div class="team-initial">${teamInitials}</div>
                </div>
                <div class="team-info">
                    <h3 class="team-name">${teamName}</h3>
                    <p class="team-league">${team.strLeague || 'NBA'}</p>
                    <p class="team-division">${team.strDivision || 'Conference'}</p>
                </div>
                <div class="team-stats">
                    <div class="stat-item">
                        <span class="stat-label">Founded</span>
                        <span class="stat-value">${team.intFormedYear || 'N/A'}</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">Stadium</span>
                        <span class="stat-value">${(team.strStadium || 'N/A').substring(0, 20)}${team.strStadium && team.strStadium.length > 20 ? '...' : ''}</span>
                    </div>
                </div>
            </div>
        `;
    }

    renderPlayerCard(player) {
        const playerName = player.strPlayer || 'Unknown Player';
        const playerPhoto = player.strThumb || player.strCutout;
        
        return `
            <div class="card player-card" data-player-id="${player.idPlayer}" title="Click to view ${playerName} details">
                <div class="player-header">
                    <div class="player-photo">
                        ${playerPhoto ? 
                            `<img src="${playerPhoto}" alt="${playerName}" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
                             <div class="player-initial" style="display:none;">${playerName.charAt(0)}</div>` :
                            `<div class="player-initial">${playerName.charAt(0)}</div>`
                        }
                    </div>
                    <div class="player-info">
                        <h3 class="player-name">${playerName}</h3>
                        <p class="player-team">${player.strTeam || 'Free Agent'}</p>
                        <p class="player-position">${player.strPosition || 'Player'}</p>
                    </div>
                </div>
                <div class="player-details">
                    <div class="detail-item">
                        <span class="detail-label">Nationality</span>
                        <span class="detail-value">${player.strNationality || 'N/A'}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Born</span>
                        <span class="detail-value">${player.dateBorn ? new Date(player.dateBorn).getFullYear() : 'N/A'}</span>
                    </div>
                </div>
            </div>
        `;
    }

    async loadTeamsPage() {
        const mainContent = document.getElementById('main-content');
        mainContent.innerHTML = '<div class="loading-container"><div class="loading-spinner"></div><p>Loading all NBA teams...</p></div>';
        
        try {
            const teams = await this.api.fetchTeams();
            mainContent.innerHTML = `
                <div class="page-header">
                    <div class="container">
                        <h1>All NBA Teams</h1>
                        <p>Complete roster of ${teams.length} NBA teams</p>
                    </div>
                </div>
                <div class="container">
                    <div class="teams-grid">
                        ${teams.map(team => this.renderTeamCard(team)).join('')}
                    </div>
                </div>
            `;
        } catch (error) {
            this.showError('Failed to load teams data');
        }
    }

    async loadPlayersPage() {
        const mainContent = document.getElementById('main-content');
        mainContent.innerHTML = '<div class="loading-container"><div class="loading-spinner"></div><p>Loading featured players...</p></div>';
        
        try {
            const players = await this.api.getFeaturedPlayers();
            mainContent.innerHTML = `
                <div class="page-header">
                    <div class="container">
                        <h1>Featured NBA Players</h1>
                        <p>Top players from around the league</p>
                    </div>
                </div>
                <div class="container">
                    <div class="players-grid">
                        ${players.map(player => this.renderPlayerCard(player)).join('')}
                    </div>
                </div>
            `;
        } catch (error) {
            this.showError('Failed to load players data');
        }
    }

    showComingSoon(page) {
        const mainContent = document.getElementById('main-content');
        mainContent.innerHTML = `
            <div class="coming-soon">
                <div class="container">
                    <h1>🚧 Coming Soon</h1>
                    <p>The ${page} page is under development.</p>
                    <button class="btn btn-primary" onclick="app.navigateToPage('home')">Back to Home</button>
                </div>
            </div>
        `;
    }

    showError(message) {
        const mainContent = document.getElementById('main-content');
        mainContent.innerHTML = `
            <div class="error-container">
                <div class="container">
                    <h2>⚠️ Error</h2>
                    <p>${message}</p>
                    <button class="btn btn-primary" onclick="location.reload()">Retry</button>
                </div>
            </div>
        `;
    }

    setupInteractivity() {
        // Add click handlers for team cards
        document.addEventListener('click', (e) => {
            const teamCard = e.target.closest('.team-card');
            if (teamCard) {
                const teamId = teamCard.dataset.teamId;
                this.showTeamDetails(teamId);
            }

            const playerCard = e.target.closest('.player-card');
            if (playerCard) {
                const playerId = playerCard.dataset.playerId;
                this.showPlayerDetails(playerId);
            }
        });
    }

    showTeamDetails(teamId) {
        // Add team details modal or navigation
        console.log(`Show details for team ${teamId}`);
        // For now, just show an alert - we can enhance this later
        alert(`Team details for ID: ${teamId} - Feature coming soon!`);
    }

    showPlayerDetails(playerId) {
        // Add player details modal or navigation
        console.log(`Show details for player ${playerId}`);
        // For now, just show an alert - we can enhance this later
        alert(`Player details for ID: ${playerId} - Feature coming soon!`);
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.app = new NBAApp();
});
