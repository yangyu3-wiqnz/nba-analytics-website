#!/usr/bin/env python3
"""
Export sample NBA data from TheSportsDB to CSV for local review
This script fetches team data and player data samples for analysis

NOTE: Due to limitations in TheSportsDB's team-based player search API 
(which returns soccer players for NBA team names), this script uses a 
curated list of known NBA players to get basketball player samples.
"""

import requests
import pandas as pd
import json
from datetime import datetime
import os

def fetch_nba_teams():
    """Fetch all NBA teams from TheSportsDB"""
    print("Fetching NBA teams from TheSportsDB...")
    url = "https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=NBA"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if 'teams' in data and data['teams']:
            print(f"✅ Successfully fetched {len(data['teams'])} teams")
            return data['teams']
        else:
            print("⚠️ No teams found in response")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching teams: {e}")
        return []

def get_sample_nba_players():
    """Get a sample of current NBA players by searching for known stars"""
    print("Fetching sample NBA players by searching for known current players...")
    
    # Known current NBA stars - this will give us a good sample
    known_players = [
        "LeBron James", "Stephen Curry", "Kevin Durant", "Giannis Antetokounmpo",
        "Jayson Tatum", "Luka Doncic", "Nikola Jokic", "Joel Embiid",
        "Jimmy Butler", "Kawhi Leonard", "Damian Lillard", "Anthony Davis",
        "Ja Morant", "Trae Young", "Devin Booker", "Donovan Mitchell",
        "Zion Williamson", "Paolo Banchero", "Victor Wembanyama", "Scottie Barnes"
    ]
    
    all_players = []
    found_player_ids = set()  # Track player IDs to avoid duplicates
    
    for player_name in known_players:
        try:
            url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={player_name}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if 'player' in data and data['player']:
                # Find the basketball player among results
                for player in data['player']:
                    if (player.get('strSport', '').lower() == 'basketball' and 
                        player.get('idPlayer') not in found_player_ids):
                        print(f"✅ Found {player.get('strPlayer')} - {player.get('strTeam')}")
                        all_players.append(player)
                        found_player_ids.add(player.get('idPlayer'))
                        break  # Take the first basketball match
                        
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching {player_name}: {e}")
            continue
    
    print(f"Successfully collected {len(all_players)} unique NBA players")
    return all_players

def export_teams_to_csv(teams, filename="../data/sample_nba_teams.csv"):
    """Export teams data to CSV"""
    if not teams:
        print("No teams data to export")
        return
    
    # Create a clean DataFrame with relevant columns
    team_data = []
    for team in teams:
        team_info = {
            'team_id': team.get('idTeam'),
            'team_name': team.get('strTeam'),
            'team_short': team.get('strTeamShort'),
            'alternate_name': team.get('strAlternate'),
            'founded': team.get('intFormedYear'),
            'stadium': team.get('strStadium'),
            'stadium_capacity': team.get('intStadiumCapacity'),
            'stadium_location': team.get('strStadiumLocation'),
            'league': team.get('strLeague'),
            'division': team.get('strDivision'),
            'manager': team.get('strManager'),
            'website': team.get('strWebsite'),
            'facebook': team.get('strFacebook'),
            'twitter': team.get('strTwitter'),
            'instagram': team.get('strInstagram'),
            'description': team.get('strDescriptionEN', '')[:200] + '...' if team.get('strDescriptionEN') else '',
            'jersey_colors': f"{team.get('strColour1', '')} / {team.get('strColour2', '')} / {team.get('strColour3', '')}".strip(' / '),
            'logo_url': team.get('strTeamLogo'),
            'badge_url': team.get('strTeamBadge')
        }
        team_data.append(team_info)
    
    # Create DataFrame and export to CSV
    df = pd.DataFrame(team_data)
    df.to_csv(filename, index=False)
    print(f"✅ Teams data exported to {filename}")
    print(f"   Exported {len(df)} teams with {len(df.columns)} columns")
    return df

def export_players_to_csv(all_players, filename="../data/sample_nba_players.csv"):
    """Export players data to CSV"""
    if not all_players:
        print("No players data to export")
        return
    
    print(f"Exporting {len(all_players)} basketball players")
    
    # Create a clean DataFrame with relevant columns
    player_data = []
    for player in all_players:
        player_info = {
            'player_id': player.get('idPlayer'),
            'player_name': player.get('strPlayer'),
            'team': player.get('strTeam'),
            'sport': player.get('strSport'),
            'position': player.get('strPosition'),
            'nationality': player.get('strNationality'),
            'birth_date': player.get('dateBorn'),
            'birth_location': player.get('strBirthLocation'),
            'height': player.get('strHeight'),
            'weight': player.get('strWeight'),
            'jersey_number': player.get('strNumber'),
            'signing_date': player.get('dateSigned'),
            'wage': player.get('strWage'),
            'description': player.get('strDescriptionEN', '')[:200] + '...' if player.get('strDescriptionEN') else '',
            'thumb_url': player.get('strThumb'),
            'cutout_url': player.get('strCutout'),
            'fanart_url': player.get('strFanart1'),
            'website': player.get('strWebsite'),
            'facebook': player.get('strFacebook'),
            'twitter': player.get('strTwitter'),
            'instagram': player.get('strInstagram')
        }
        player_data.append(player_info)
    
    # Create DataFrame and export to CSV
    df = pd.DataFrame(player_data)
    df.to_csv(filename, index=False)
    print(f"✅ Players data exported to {filename}")
    print(f"   Exported {len(df)} players with {len(df.columns)} columns")
    return df

def create_data_summary(teams_df, players_df):
    """Create a summary report of the exported data"""
    summary_filename = "../data/sample_data_summary.txt"
    
    with open(summary_filename, 'w') as f:
        f.write("NBA Sample Data Export Summary\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Data Source: TheSportsDB API\n\n")
        
        f.write("TEAMS DATA:\n")
        f.write("-" * 20 + "\n")
        if teams_df is not None:
            f.write(f"Total Teams: {len(teams_df)}\n")
            f.write(f"Columns: {len(teams_df.columns)}\n")
            f.write(f"Teams with Stadiums: {teams_df['stadium'].notna().sum()}\n")
            f.write(f"Teams with Descriptions: {teams_df['description'].str.len().gt(10).sum()}\n")
            f.write(f"Sample Teams: {', '.join(teams_df['team_name'].head(5).tolist())}\n\n")
        
        f.write("PLAYERS DATA:\n")
        f.write("-" * 20 + "\n")
        if players_df is not None:
            f.write(f"Total Players: {len(players_df)}\n")
            f.write(f"Columns: {len(players_df.columns)}\n")
            f.write(f"Players with Positions: {players_df['position'].notna().sum()}\n")
            f.write(f"Players with Birth Dates: {players_df['birth_date'].notna().sum()}\n")
            f.write(f"Different Teams Represented: {players_df['team'].nunique()}\n")
            
            # Position breakdown
            position_counts = players_df['position'].value_counts().head(5)
            f.write(f"Top Positions: {dict(position_counts)}\n\n")
        
        f.write("FILES CREATED:\n")
        f.write("-" * 20 + "\n")
        f.write("- ../data/sample_nba_teams.csv\n")
        f.write("- ../data/sample_nba_players.csv\n")
        f.write("- ../data/sample_data_summary.txt\n\n")
        
        f.write("USAGE:\n")
        f.write("-" * 20 + "\n")
        f.write("- These files are for local review and analysis\n")
        f.write("- CSV files can be opened in Excel, Google Sheets, or any data tool\n")
        f.write("- Use this data to understand the structure and quality of TheSportsDB\n")
        f.write("- Files are git-ignored for privacy and repository size management\n")
    
    print(f"✅ Data summary created: {summary_filename}")

def main():
    """Main execution function"""
    print("🏀 NBA Sample Data Export from TheSportsDB")
    print("=" * 50)
    
    # Fetch teams data
    teams = fetch_nba_teams()
    teams_df = export_teams_to_csv(teams) if teams else None
    
    # Fetch players data using a sample of known NBA players
    all_players = get_sample_nba_players()
    
    players_df = export_players_to_csv(all_players) if all_players else None
    
    # Create summary
    create_data_summary(teams_df, players_df)
    
    print("\n🎉 Sample data export complete!")
    print("\nFiles created:")
    print("- ../data/sample_nba_teams.csv (Team information)")
    print("- ../data/sample_nba_players.csv (Player information)")
    print("- ../data/sample_data_summary.txt (Export summary)")
    print("\nThese files are now available for local review.")

if __name__ == "__main__":
    # Install required packages if not available
    try:
        import pandas
    except ImportError:
        print("Installing required packages...")
        os.system("pip install pandas requests")
        import pandas as pd
    
    main()
