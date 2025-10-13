
class ManageTournamentView:
    # Shows name, venue, dates, number of rounds, current round, completion status, and registered players.
    def display_tournament_details(self, tournament):
        print("\n*** Tournament Details ***")
        print(f"Name: {tournament.name}")
        print(f"Venue: {tournament.venue}")
        print(f"Dates: {tournament.dates.start} to {tournament.dates.end}")
        print(f"Rounds: {tournament.total_rounds}")
        print(f"Current Round: {tournament.current_round or 'None'}")
        print(f"Completed: {'Yes' if tournament.completed else 'No'}")
        print("Players:")
        for player in tournament.registered_players:
            print(f"- {player.name} ({player.chess_id})")

    # Lists actions the user can take (register player, enter results, etc.).
    def display_manage_options(self):
        print("\n1. Register a player")
        print("2. Enter match results")
        print("3. Advance to next round")
        print("4. Generate tournament report")
        print("5. Return to main menu")

    # Asks the user to choose one of those actions.
    def prompt_manage_choice(self):
        return input("Choose an option (1–5): ")