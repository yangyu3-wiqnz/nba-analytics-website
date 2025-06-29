// Simple API Testing Script for NBA Analytics Backend Development
// Focus: Testing external APIs and preparing for FastAPI backend development

class APITester {
    constructor() {
        this.statusIndicator = document.getElementById('status-indicator');
        this.resultsContainer = document.getElementById('api-results');
        this.initializeCharts();
    }

    // Update status indicator
    updateStatus(status, message) {
        this.statusIndicator.className = `badge bg-${status === 'loading' ? 'primary' : status === 'success' ? 'success' : 'danger'}`;
        this.statusIndicator.textContent = message;
    }

    // Display results in formatted way
    displayResults(data, endpoint = '') {
        const timestamp = new Date().toLocaleTimeString();
        let htmlContent = `
            <div class="mb-3">
                <strong>Endpoint:</strong> ${endpoint}<br>
                <strong>Time:</strong> ${timestamp}<br>
                <strong>Status:</strong> <span class="status-success">Success</span>
            </div>
            <pre style="white-space: pre-wrap; word-wrap: break-word;">${JSON.stringify(data, null, 2)}</pre>
        `;
        this.resultsContainer.innerHTML = htmlContent;
    }

    // Display error
    displayError(error, endpoint = '') {
        const timestamp = new Date().toLocaleTimeString();
        let htmlContent = `
            <div class="mb-3">
                <strong>Endpoint:</strong> ${endpoint}<br>
                <strong>Time:</strong> ${timestamp}<br>
                <strong>Status:</strong> <span class="status-error">Error</span>
            </div>
            <div class="alert alert-danger">
                <strong>Error:</strong> ${error.message || error}
            </div>
        `;
        this.resultsContainer.innerHTML = htmlContent;
    }

    // Test external NBA APIs
    async testExternalAPI(type) {
        this.updateStatus('loading', 'Loading...');
        
        let endpoint = '';
        try {
            switch(type) {
                case 'teams':
                    endpoint = 'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=NBA';
                    break;
                case 'players':
                    endpoint = 'https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?t=Lakers';
                    break;
                case 'player-stats':
                    endpoint = 'https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=LeBron%20James';
                    break;
                default:
                    throw new Error('Unknown API type');
            }

            const response = await fetch(endpoint);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const data = await response.json();
            this.updateStatus('success', 'Success');
            this.displayResults(data, endpoint);
            
            // Update charts with real data if available
            if (type === 'teams' && data.teams) {
                this.updateTeamChart(data.teams.slice(0, 5));
            }
            
        } catch (error) {
            this.updateStatus('error', 'Error');
            this.displayError(error, endpoint);
        }
    }

    // Test future backend APIs (placeholder)
    async testBackendAPI(type) {
        this.updateStatus('loading', 'Loading...');
        
        // Simulate future FastAPI endpoints
        const mockData = {
            'analytics': {
                message: "This will be your FastAPI analytics endpoint",
                example_data: {
                    top_scorers: ["LeBron James", "Stephen Curry", "Kevin Durant"],
                    avg_points_per_game: 115.2,
                    total_games_analyzed: 1230
                }
            },
            'ml-predict': {
                message: "This will be your ML prediction endpoint",
                prediction: {
                    next_game_score: {"Lakers": 112, "Warriors": 108},
                    confidence: 0.78,
                    model_version: "v1.2.0"
                }
            },
            'advanced-stats': {
                message: "This will be your advanced statistics endpoint",
                stats: {
                    player_efficiency_rating: 28.5,
                    true_shooting_percentage: 0.641,
                    usage_rate: 0.325
                }
            }
        };

        setTimeout(() => {
            this.updateStatus('success', 'Mock Success');
            this.displayResults(mockData[type], `Future: /api/${type}`);
        }, 1000);
    }

    // Test custom endpoint
    async testCustomAPI() {
        const endpoint = document.getElementById('apiEndpoint').value.trim();
        if (!endpoint) {
            alert('Please enter an API endpoint to test');
            return;
        }

        this.updateStatus('loading', 'Testing...');
        
        try {
            const response = await fetch(endpoint);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const data = await response.json();
            this.updateStatus('success', 'Success');
            this.displayResults(data, endpoint);
            
        } catch (error) {
            this.updateStatus('error', 'Error');
            this.displayError(error, endpoint);
        }
    }

    // Initialize sample charts
    initializeCharts() {
        // Team Chart
        const teamCtx = document.getElementById('teamChart');
        if (teamCtx) {
            this.teamChart = new Chart(teamCtx, {
                type: 'bar',
                data: {
                    labels: ['Lakers', 'Warriors', 'Celtics', 'Heat', 'Bulls'],
                    datasets: [{
                        label: 'Wins',
                        data: [45, 42, 48, 40, 35],
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Sample Team Wins (Mock Data)'
                        }
                    }
                }
            });
        }

        // Player Chart
        const playerCtx = document.getElementById('playerChart');
        if (playerCtx) {
            this.playerChart = new Chart(playerCtx, {
                type: 'line',
                data: {
                    labels: ['Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5'],
                    datasets: [{
                        label: 'Points Scored',
                        data: [28, 32, 25, 35, 30],
                        borderColor: 'rgba(255, 99, 132, 1)',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        tension: 0.1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Sample Player Performance (Mock Data)'
                        }
                    }
                }
            });
        }
    }

    // Update team chart with real data
    updateTeamChart(teams) {
        if (this.teamChart && teams) {
            const teamNames = teams.map(team => team.strTeam || 'Unknown').slice(0, 5);
            const randomData = teams.map(() => Math.floor(Math.random() * 50) + 20);
            
            this.teamChart.data.labels = teamNames;
            this.teamChart.data.datasets[0].data = randomData;
            this.teamChart.data.datasets[0].label = 'Sample Data (Random)';
            this.teamChart.options.plugins.title.text = 'Real Team Names with Mock Data';
            this.teamChart.update();
        }
    }

    // Generate sample charts for demonstration
    generateSampleCharts() {
        this.updateStatus('success', 'Charts Generated');
        
        // Update with different sample data
        if (this.teamChart) {
            this.teamChart.data.datasets[0].data = [Math.random() * 50, Math.random() * 50, Math.random() * 50, Math.random() * 50, Math.random() * 50];
            this.teamChart.update();
        }
        
        if (this.playerChart) {
            this.playerChart.data.datasets[0].data = [Math.random() * 40, Math.random() * 40, Math.random() * 40, Math.random() * 40, Math.random() * 40];
            this.playerChart.update();
        }
        
        this.displayResults({
            message: "Sample charts updated with new random data",
            note: "In your FastAPI backend, these will show real analytics and ML predictions",
            focus: "Backend development, database optimization, and machine learning"
        }, "Chart Generation");
    }

    // Show data summary
    showDataSummary() {
        const summary = {
            project_focus: "Backend Development & Data Analysis",
            technologies: {
                backend: ["FastAPI", "PostgreSQL", "SQLAlchemy", "Alembic"],
                data: ["Pandas", "NumPy", "Scikit-learn"],
                deployment: ["Docker", "Redis", "Celery"],
                frontend: ["Vanilla JS", "Bootstrap", "Chart.js"]
            },
            next_steps: [
                "Set up FastAPI project structure",
                "Design PostgreSQL database schema",
                "Create data ingestion pipelines",
                "Build REST API endpoints",
                "Implement machine learning models",
                "Add comprehensive testing"
            ],
            learning_goals: [
                "API development best practices",
                "Database optimization techniques",
                "Data pipeline architecture",
                "ML model deployment",
                "Performance monitoring"
            ]
        };
        
        this.updateStatus('success', 'Summary Generated');
        this.displayResults(summary, "Project Summary");
    }
}

// Global functions for HTML onclick events
let apiTester;

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    apiTester = new APITester();
});

// Global functions for button clicks
function testExternalAPI(type) {
    apiTester.testExternalAPI(type);
}

function testBackendAPI(type) {
    apiTester.testBackendAPI(type);
}

function testCustomAPI() {
    apiTester.testCustomAPI();
}

function generateSampleCharts() {
    apiTester.generateSampleCharts();
}

function showDataSummary() {
    apiTester.showDataSummary();
}
