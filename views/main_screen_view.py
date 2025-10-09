# Handles the entry point of the app. Displays available tournaments and lets the user choose one or create a new one.

class MainScreenView:
    def display_tournament_list(self, tournaments):
        print("\n*** Available Tournaments ***")
        # Lambda use : for each tournament t, extract its dates.start value to use as the sorting key.
        # Sort in descending order
        sorted_tournaments = sorted(tournaments, key=lambda t: t.dates.start, reverse=True)
        # Loop through the sorted tournaments and print each one with a number for selection.
        for i, t in enumerate(sorted_tournaments, start=1):
            print(f"{i}. {t.name} ({t.dates.start} to {t.dates.end})")

    # Number generated from previous function
    def prompt_tournament_selection(self):
        return input("Select a tournament by number or type 'new' to create one: ")

    # Fallback message if no tournaments exist
    def display_no_tournaments_message(self):
        print("No tournaments available. Please create a new one.")