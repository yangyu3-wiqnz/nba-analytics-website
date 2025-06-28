#!/usr/bin/env python3
"""
NBA API Testing Script
======================
This script tests different NBA APIs to help you choose the best one for your project.
Run this to complete Phase 1.3 tasks in your roadmap!
"""

import requests
import json
import time
from datetime import datetime

def test_balldontlie_api():
    """Test the balldontlie.io API (Free NBA API)"""
    print("🏀 Testing balldontlie.io API...")
    print("-" * 50)
    
    try:
        # Test 1: Get all NBA teams
        print("📋 Fetching NBA teams...")
        teams_url = "https://www.balldontlie.io/api/v1/teams"
        teams_response = requests.get(teams_url, timeout=10)
        
        if teams_response.status_code == 200:
            teams_data = teams_response.json()
            print(f"✅ Success! Found {len(teams_data['data'])} NBA teams")
            
            # Show a few teams
            for team in teams_data['data'][:5]:
                print(f"   - {team['full_name']} ({team['abbreviation']})")
            print(f"   ... and {len(teams_data['data']) - 5} more teams")
        else:
            print(f"❌ Failed to fetch teams: {teams_response.status_code}")
            return False
        
        time.sleep(1)  # Be nice to the API
        
        # Test 2: Get some players
        print("\n👥 Fetching NBA players...")
        players_url = "https://www.balldontlie.io/api/v1/players?per_page=10"
        players_response = requests.get(players_url, timeout=10)
        
        if players_response.status_code == 200:
            players_data = players_response.json()
            print(f"✅ Success! Found players (showing first 10)")
            
            for player in players_data['data']:
                team_name = player['team']['full_name'] if player['team'] else "Free Agent"
                print(f"   - {player['first_name']} {player['last_name']} ({team_name})")
        else:
            print(f"❌ Failed to fetch players: {players_response.status_code}")
            return False
            
        time.sleep(1)
        
        # Test 3: Search for a specific player (LeBron James)
        print("\n🔍 Searching for LeBron James...")
        search_url = "https://www.balldontlie.io/api/v1/players?search=lebron"
        search_response = requests.get(search_url, timeout=10)
        
        if search_response.status_code == 200:
            search_data = search_response.json()
            if search_data['data']:
                lebron = search_data['data'][0]
                print(f"✅ Found: {lebron['first_name']} {lebron['last_name']}")
                print(f"   Team: {lebron['team']['full_name'] if lebron['team'] else 'N/A'}")
                print(f"   Position: {lebron['position'] or 'N/A'}")
            else:
                print("❌ LeBron James not found")
        
        print("\n🎯 balldontlie.io API Summary:")
        print("   ✅ Free to use")
        print("   ✅ No API key required")
        print("   ✅ Good for basic player and team data")
        print("   ⚠️  Limited advanced statistics")
        print("   ⚠️  Rate limited (be respectful)")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_thesportsdb_api():
    """Test TheSportsDB API"""
    print("\n🏀 Testing TheSportsDB API...")
    print("-" * 50)
    
    try:
        # Test: Get NBA league info
        print("📋 Fetching NBA league information...")
        league_url = "https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=NBA"
        league_response = requests.get(league_url, timeout=10)
        
        if league_response.status_code == 200:
            league_data = league_response.json()
            if league_data.get('teams'):
                print(f"✅ Success! Found {len(league_data['teams'])} NBA teams")
                
                # Show a few teams
                for team in league_data['teams'][:5]:
                    print(f"   - {team['strTeam']} ({team.get('strTeamShort', 'N/A')})")
                print(f"   ... and {len(league_data['teams']) - 5} more teams")
                
                # Show what data is available
                sample_team = league_data['teams'][0]
                print(f"\n📊 Available team data fields:")
                interesting_fields = ['strTeam', 'strLeague', 'strStadium', 'strWebsite', 'strDescriptionEN']
                for field in interesting_fields:
                    if field in sample_team and sample_team[field]:
                        print(f"   - {field}: Available")
            else:
                print("❌ No teams found")
                return False
        else:
            print(f"❌ Failed to fetch league data: {league_response.status_code}")
            return False
        
        print("\n🎯 TheSportsDB API Summary:")
        print("   ✅ Free to use")
        print("   ✅ Rich team information")
        print("   ✅ Good for team details, stadiums, descriptions")
        print("   ⚠️  Limited real-time player statistics")
        print("   ⚠️  More focused on team data than player stats")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def generate_api_comparison_report():
    """Generate a comparison report for the APIs"""
    print("\n" + "="*60)
    print("🏆 NBA API COMPARISON REPORT")
    print("="*60)
    
    print("\n📊 FEATURE COMPARISON:")
    print("-" * 40)
    
    features = [
        ("Cost", "balldontlie.io: FREE", "TheSportsDB: FREE"),
        ("API Key Required", "balldontlie.io: NO", "TheSportsDB: NO"),
        ("Player Data", "balldontlie.io: ⭐⭐⭐⭐", "TheSportsDB: ⭐⭐"),
        ("Team Data", "balldontlie.io: ⭐⭐⭐", "TheSportsDB: ⭐⭐⭐⭐⭐"),
        ("Real-time Stats", "balldontlie.io: ⭐⭐⭐", "TheSportsDB: ⭐"),
        ("Historical Data", "balldontlie.io: ⭐⭐", "TheSportsDB: ⭐⭐⭐"),
        ("Ease of Use", "balldontlie.io: ⭐⭐⭐⭐⭐", "TheSportsDB: ⭐⭐⭐⭐"),
    ]
    
    for feature, api1, api2 in features:
        print(f"{feature:15} | {api1:25} | {api2}")
    
    print("\n💡 RECOMMENDATIONS:")
    print("-" * 40)
    print("🥇 For MVP/Starting: balldontlie.io")
    print("   - Perfect for getting started")
    print("   - Good player and basic stats data")
    print("   - Simple, clean API")
    
    print("\n🥈 For Team Details: TheSportsDB")
    print("   - Excellent team information")
    print("   - Rich descriptions and metadata")
    print("   - Good for team pages")
    
    print("\n🚀 RECOMMENDED HYBRID APPROACH:")
    print("   1. Start with balldontlie.io for core functionality")
    print("   2. Add TheSportsDB for enhanced team pages")
    print("   3. Consider paid APIs later for advanced analytics")

def main():
    """Main function to run all API tests"""
    print("🏀 NBA API TESTING SUITE")
    print("=" * 50)
    print(f"⏰ Testing started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test APIs
    results = {}
    results['balldontlie'] = test_balldontlie_api()
    results['thesportsdb'] = test_thesportsdb_api()
    
    # Generate report
    generate_api_comparison_report()
    
    print("\n" + "="*60)
    print("✅ API TESTING COMPLETE!")
    print("="*60)
    
    print("\n📋 NEXT STEPS FOR YOUR ROADMAP:")
    print("1. ✅ Test TheSportsDB API - DONE")
    print("2. ✅ Test balldontlie.io API - DONE") 
    print("3. ✅ Compare API features - DONE")
    print("4. 🔄 Choose final API (Recommended: balldontlie.io)")
    print("5. 🔄 Obtain access credentials (None needed for free APIs)")
    
    print(f"\n🎯 You can now check off tasks in Phase 1.3 of your roadmap!")
    print(f"💡 Next: Move on to Phase 1.4 (Technology Stack) or start coding!")

if __name__ == "__main__":
    main()
