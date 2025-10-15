from models.tournament import Tournament
from models.dates import Dates

# TournamentService is a helper class that acts as a data layer between the controller and models
# This offloads logic from the controller
"""
This service:
- Keeps a list of tournaments in memory
- Filters for active tournaments (not completed)
- Prompts the user to create a new tournament and returns it to the controller
"""
class TournamentService:
    # Initialize an in-memory list for now. 
    def __init__(self):
        self.tournaments = [] # This can be replaced with loading from a JSON file

    # Returns the full list of tournaments. 
    # Used by controller to display all tournaments on the main screen.
    def get_all_tournaments(self):
        return self.tournaments

    # Filters tournaments that are not completed.
    # Useful when deciding whether to jump straight into managing an active tournament.
    def get_active_tournaments(self):
        return [t for t in self.tournaments if t.is_active()]

    # Prompts user for tournament details
    def create_tournament(self):
        print("\n*** Create New Tournament ***")
        name = input("Tournament name: ")
        venue = input("Venue: ")
        start = input("Start date (YYYY-MM-DD): ")
        end = input("End date (YYYY-MM-DD): ")
        total_rounds = int(input("Number of rounds: "))
        # Create a date object and tournament instance
        dates = Dates(start, end)
        tournament = Tournament(name, venue, dates, registered_players=[], total_rounds=total_rounds)
        self.tournaments.append(tournament)

        print(f"Tournament '{name}' created successfully.")
        return tournament