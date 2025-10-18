# Display a summary report of the tournament


class TournamentReportView:
    # Displays full report
    def display_report(self, tournament, scores):
        print("\n*** Tournament Report ***")
        print(f"Name: {tournament.name}")
        print(f"Dates: {tournament.dates.start} to {tournament.dates.end}")
        print("\nPlayers by Score:")
        # Sorts the dictionary of scores by the score value (not the player ID)
        # For each (player_id, score) tuple x, return the score (x[1]) to use as the sorting key
        for player_id, score in sorted(
            scores.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"{player_id}: {score} points")

        print("\nRounds and Matches:")
        # Outer loop: for each round
        for i, round_obj in enumerate(tournament.rounds, start=1):
            print(f"\nRound {i}:")
            # Inner loop: for each match in that round
            for match in round_obj.matches:
                p1, p2 = match.players
                result = match.winner_id or "Draw"
                print(f"- {p1} vs {p2} → {result}")
