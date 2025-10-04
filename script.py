import json
from models.player import Player
from models.tournament import Tournament
from models.dates import Dates
from datetime import datetime

# Load players from JSON files
def load_players():
    player_files = ["data/clubs/cornville.json","data/clubs/springfield.json"]
    # List to store combined player objects
    all_players = []
    # Loop through each JSON file containing the club-specific players
    for file_path in player_files:
        with open(file_path, "r") as f:
            data = json.load(f) # read JSON structure
            player_dicts = data.get("players", []) # extract the players list under the "players" key
            # convert each dictionary into a Player object and add to all_players list
            all_players.extend([Player(**player) for player in player_dicts])

    return all_players

# Ask for Chess ID and display player info
def find_player_by_id(players):
    chess_id = input("Enter Chess ID: ")
    for player in players:
        if player.chess_id == chess_id:
            print(f"Name: {player.name}, Email: {player.email}, Birthday: {player.birthday}")
            return
    print("Player not found.")

# Load a tournament and display its basic attributes (no rounds or player information)
def load_tournament(): 
    with open("data/tournaments/completed.json", "r") as f:
        data = json.load(f) #parse content into Python dictionary

    # Parse dates
    start_date = datetime.strptime(data["dates"]["from"], "%d-%m-%Y").date()
    end_date = datetime.strptime(data["dates"]["to"], "%d-%m-%Y").date()
    dates = Dates(start_date, end_date)

    # Create tournament object
    tournament = Tournament(
        data["name"],
        data["venue"],
        dates,
        data["players"],
        data["number_of_rounds"],
    )
    tournament.completed = data.get("completed", False) # set to False if key is missing

    # Display basic attributes only
    print(f"Tournament Name: {tournament.name}")
    print(f"Venue: {tournament.venue}")
    print(f"Dates: {tournament.dates.start_date} to {tournament.dates.end_date}")
    print(f"Number of Rounds: {tournament.total_rounds}")
    print(f"Number of Registered Players: {len(tournament.registered_players)}")
    print(f"Completed: {tournament.completed}")

    return tournament
# Test output
load_tournament()

def load_completed_tournament()
    with open("data/tournaments/completed.json", "r") as f:
        data = json.load(f) #parse content into Python dictionary

    # Parse dates
    start_date = datetime.strptime(data["dates"]["from"], "%d-%m-%Y").date()
    end_date = datetime.strptime(data["dates"]["to"], "%d-%m-%Y").date()
    dates = Dates(start_date, end_date)

    # Create tournament object
    tournament = Tournament(
        data["name"],
        data["venue"],
        dates,
        data["players"],
        data["number_of_rounds"],
    )
    tournament.completed = data.get("completed", False) # set to False if key is missing

    # Initialize scores
    scores = {player_id: 0 for player_id in data["players"]}

    # Rebuild rounds and calculate scores
    for round_data in data.get("rounds", []):
        for match_data in round_data:
            p1, p2 = match_data["players"]
            winner = match_data["winner"]

            if winner is None:
                scores[p1] += 0.5
                scores[p2] += 0.5
            else:
                scores[winner] += 1
                loser = p1 if winner == p2 else p2
                scores[loser] += 0  # Explicit for clarity

    # Display basic attributes only
    print(f"Tournament Name: {tournament.name}")
    print(f"Venue: {tournament.venue}")
    print(f"Dates: {tournament.dates.start_date} to {tournament.dates.end_date}")
    print(f"Number of Rounds: {tournament.total_rounds}")
    print(f"Number of Registered Players: {len(tournament.registered_players)}")
    print(f"Completed: {tournament.completed}")

    # Display final scores
    print("\nFinal Scores:")
    for player_id, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{player_id}: {score} points")




