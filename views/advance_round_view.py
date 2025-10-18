# Handles the confirmation and progression to the next round.


class AdvanceRoundView:
    # Asks the user to confirm advancing to the next round.
    def prompt_confirmation(self):
        return input("Are you sure you want to advance to the next round? (yes/no): ")

    # Confirms that the new round has started.
    def display_round_advanced(self, round_number):
        print(f"Round {round_number} has started.")

    # Announces that the tournament is finished.
    def display_tournament_completed(self):
        print("Tournament has ended. All rounds completed.")
