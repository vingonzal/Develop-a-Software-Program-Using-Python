import json
from models.player import Player
from models.tournament import Tournament
from models.dates import Dates
from datetime import date

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
        data = json.load(f)

    # Parse dates
    start_date = datetime.strptime(data["dates"]["from"], "%d-%m-%Y").date()
    end_date = datetime.strptime(data["dates"]["to"], "%d-%m-%Y").date()
    dates = Dates(start=start_date, end=end_date)

    # Create tournament object
    tournament = Tournament(
        name=data["name"],
        venue=data["venue"],
        dates=dates,
        registered_players=data["players"],
        total_rounds=data["number_of_rounds"]
    )
    tournament.completed = data.get("completed", False)

    # Display basic attributes only
    print(f"Tournament Name: {tournament.name}")
    print(f"Venue: {tournament.venue}")
    print(f"Dates: {tournament.dates.start} to {tournament.dates.end}")
    print(f"Number of Rounds: {tournament.total_rounds}")
    print(f"Completed: {tournament.completed}")

    return tournament






