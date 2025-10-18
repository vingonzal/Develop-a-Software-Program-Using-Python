# Allows the user to search for and register players to the tournament.


class RegisterPlayerView:
    # Shows all available players with their name and chess ID.
    def display_player_list(self, players):
        print("\n*** Available Players ***")
        for i, player in enumerate(players, start=1):
            print(f"{i}. {player.name} ({player.chess_id})")

    # Let's the user choose to search by chess ID or name.
    def prompt_search_method(self):
        print("\nSearch by:")
        print("1. Chess ID")
        print("2. Name")
        return input("Choose search method (1 or 2): ")

    # Collects the actual search term
    def prompt_search_query(self):
        return input("Enter search query: ")

    # Lets the user pick a player to register or go back.
    def prompt_player_selection(self):
        return input(
            "Select a player by number to register, or type 'back' to return: "
        )

    # Confirms that a player has been registered
    def confirm_registration(self, player):
        print(f"{player.name} has been registered for the tournament.")
