import json
from models.player import Player
from models.tournament import Tournament
from models.dates import Dates
from datetime import date

# Load players from JSON files
def load_players():
    player_files = [
        "data/clubs/cornville.json",
        "data/clubs/springfield.json"
    ]
    all_players = []

    for file_path in player_files:
        with open(file_path, "r") as f:
            data = json.load(f)
            player_dicts = data.get("players", [])
            all_players.extend([Player(**player) for player in player_dicts])

    return all_players

