/**
 * NBA Data API Client
 * Handles fetching live data from TheSportsDB API
 */

class NBADataAPI {
    constructor() {
        this.baseURL = 'https://www.thesportsdb.com/api/v1/json/3';
        this.cache = new Map();
        this.cacheTimeout = 5 * 60 * 1000; // 5 minutes
    }

    /**
     * Fetch all NBA teams
     */
    async fetchTeams() {
        const cacheKey = 'nba_teams';
        
        // Check cache first
        if (this.cache.has(cacheKey)) {
            const cached = this.cache.get(cacheKey);
            if (Date.now() - cached.timestamp < this.cacheTimeout) {
                return cached.data;
            }
        }

        try {
            const response = await fetch(`${this.baseURL}/search_all_teams.php?l=NBA`);
            const data = await response.json();
            
            if (data.teams) {
                // Cache the result
                this.cache.set(cacheKey, {
                    data: data.teams,
                    timestamp: Date.now()
                });
                return data.teams;
            }
            
            throw new Error('No teams found');
        } catch (error) {
            console.error('Error fetching teams:', error);
            return [];
        }
    }

    /**
     * Search for a specific player
     */
    async searchPlayer(playerName) {
        const cacheKey = `player_${playerName}`;
        
        if (this.cache.has(cacheKey)) {
            const cached = this.cache.get(cacheKey);
            if (Date.now() - cached.timestamp < this.cacheTimeout) {
                return cached.data;
            }
        }

        try {
            const response = await fetch(`${this.baseURL}/searchplayers.php?p=${encodeURIComponent(playerName)}`);
            const data = await response.json();
            
            if (data.player) {
                // Filter for basketball players only
                const basketballPlayers = data.player.filter(
                    player => player.strSport && player.strSport.toLowerCase() === 'basketball'
                );
                
                this.cache.set(cacheKey, {
                    data: basketballPlayers,
                    timestamp: Date.now()
                });
                
                return basketballPlayers;
            }
            
            return [];
        } catch (error) {
            console.error(`Error searching for player ${playerName}:`, error);
            return [];
        }
    }

    /**
     * Get featured NBA players (current stars)
     */
    async getFeaturedPlayers() {
        const featuredPlayerNames = [
            'LeBron James', 'Stephen Curry', 'Kevin Durant', 
            'Giannis Antetokounmpo', 'Jayson Tatum', 'Luka Doncic'
        ];

        const playerPromises = featuredPlayerNames.map(name => this.searchPlayer(name));
        const playerResults = await Promise.all(playerPromises);
        
        // Get the first basketball player from each search
        return playerResults
            .map(players => players[0])
            .filter(player => player); // Remove undefined results
    }

    /**
     * Get team details by team name
     */
    async getTeamDetails(teamName) {
        const teams = await this.fetchTeams();
        return teams.find(team => 
            team.strTeam.toLowerCase().includes(teamName.toLowerCase())
        );
    }
}

// Export for use in other files
window.NBADataAPI = NBADataAPI;
