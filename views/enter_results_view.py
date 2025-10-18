# Displays matches in the current round and lets the user enter results.


class EnterResultsView:
    # Lists all matches in the current round and whether they’re completed.
    def display_current_round_matches(self, matches):
        print("\n*** Current Round Matches ***")
        # Prints each match with its status.
        for i, match in enumerate(matches, start=1):
            p1, p2 = match.player_ids
            print(
                f"{i}. {p1} vs {p2} - Result: {'Completed' if match.completed else 'Pending'}"
            )

    # Asks the user to enter the result: win for player 1, win for player 2, or draw
    def prompt_match_result(self, match):
        print(f"\nMatch: {match.player_ids[0]} vs {match.player_ids[1]}")
        print("1. Player 1 wins")
        print("2. Player 2 wins")
        print("3. Draw")
        return input("Enter result (1–3): ")

    # Confirms that the result was recorded
    def confirm_result_entry(self, match):
        print(
            f"Result recorded for match: {match.player_ids[0]} vs {match.player_ids[1]}"
        )
