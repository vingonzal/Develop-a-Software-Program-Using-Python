from models.club_manager import ClubManager
from models.tournament import Tournament
from services.player_service import PlayerService
from services.tournament_service import TournamentService
from views.enter_results_view import EnterResultsView
from views.main_screen_view import MainScreenView
from views.manage_tournament_view import ManageTournamentView
from views.register_player_view import RegisterPlayerView

# This is the controller

"""
This controller will do the following:
- Create and manage Tournament instances
- Route user input to the correct view and model methods
- Handle tournament lifecycle: creation → registration → rounds → results → report
- Coordinate the views: MainScreenView, ManageTournamentView, EnterResultsView, etc.
"""


class AppController:
    # Initializes services and views
    def __init__(self):
        self.tournament_service = TournamentService()
        self.club_manager = ClubManager("data/clubs")
        self.player_service = PlayerService(self.club_manager)
        self.register_view = RegisterPlayerView()
        self.main_view = MainScreenView()
        self.manage_view = ManageTournamentView()
        self.results_view = EnterResultsView()

    # This function is a helper method that wraps any action that modifies tournament data.
    # This will perform the update and save the data to the tournament JSON file
    """
    This ensures that every change —
    like registering a player, recording a match result, or advancing a round —
    is saved instantly, keeping in-memory data and JSON files in sync.
    """

    def save_and_update(self, update_function, *args, **kwargs):
        update_function(*args, **kwargs)
        self.tournament_service.save_tournaments()

    # Checks for active tournaments (starts the main loop)
    def run(self):
        while True:
            active_tournaments = self.tournament_service.get_active_tournaments()
            # If a tournament is active jump straight to managing it
            if len(active_tournaments) == 1:
                tournament = active_tournaments[0]
                self.manage_tournament(tournament)
            else:
                # show main screen to select or create new tournament
                self.show_main_screen()

    # Displays the main menu and handles tournament selection or creation
    def show_main_screen(self):
        # Gets all the tournaments
        tournaments = self.tournament_service.get_all_tournaments()
        # If none exist, prompt to create a new one
        if not tournaments:
            self.main_view.display_no_tournaments_message()
            selection = "new"
        # Show numbered list
        else:
            self.main_view.display_tournament_list(tournaments)
            selection = self.main_view.prompt_tournament_selection()

        if selection.lower() == "new":
            # Create new tournament object
            tournament = self.tournament_service.create_tournament()
            self.manage_tournament(tournament)  # being interaction
        else:
            # Handles invalid input/error handling
            try:
                index = int(selection) - 1  # - 1 due to zero-based indexing
                tournament = tournaments[index]  # retrieve tournament at that index
                self.manage_tournament(tournament)  # pass the tournament to the method
            except (ValueError, IndexError):
                # If input is invalid integer or index number is out of range
                print("Invalid selection. Please try again.")
                self.show_main_screen()

    # Displays tournament details and options
    def manage_tournament(self, tournament):
        # Allows users to manage the tournament continuously
        while True:
            self.manage_view.display_tournament_details(tournament)
            self.manage_view.display_manage_options()
            choice = self.manage_view.prompt_manage_choice()

            if choice == "1":
                self.register_player_to_tournament(tournament)
                print("Player registration complete.\n")
            elif choice == "2":
                self.enter_match_results(tournament)
                print("Match results updated.\n")
            elif choice == "3":
                self.advance_round(tournament)
                print("Round advanced.\n")
            elif choice == "4":
                self.generate_report(tournament)
                print("Report generated.\n")
            elif choice == "5":
                print("Returning to main menu...\n")
                break
            else:
                print("Invalid choice. Please try again.\n")

    # Handles player search and registration
    def register_player_to_tournament(self, tournament):
        players = self.player_service.get_all_players()
        self.register_view.display_player_list(players)

        method = self.register_view.prompt_search_method()
        if method == "1":
            query = self.register_view.prompt_search_query()
            player = self.player_service.search_by_chess_id(query)
            if player:
                self.save_and_update(tournament.register_player, player)
                self.register_view.confirm_registration(player)
            else:
                print("Player not found.")
        elif method == "2":
            query = self.register_view.prompt_search_query()
            results = self.player_service.search_by_name(query)
            self.register_view.display_player_list(results)
            selection = self.register_view.prompt_player_selection()
            if selection.lower() == "back":
                return
            try:
                index = int(selection) - 1
                player = results[index]
                self.save_and_update(tournament.register_player, player)
                self.register_view.confirm_registration(player)
            except (ValueError, IndexError):
                print("Invalid selection.")
        else:
            print("Invalid search method.")

    # This allows users to input match outcomes for the current round.
    # This will connect the controller to the EnterResultsView, update match results, and adjust player scores.
    def enter_match_results(self, tournament):
        if tournament.current_round == 0 or tournament.current_round > len(
            tournament.rounds
        ):
            print("No active round to enter results for.")
            return

        round_obj = tournament.rounds[tournament.current_round - 1]
        self.results_view.display_current_round_matches(round_obj.matches)

        for match in round_obj.matches:
            if match.completed:
                continue

            result = self.results_view.prompt_match_result(match)

            if result == "1":
                self.save_and_update(match.record_result, match.player_ids[0])
                tournament.scores[match.player_ids[0]] += 1
            elif result == "2":
                self.save_and_update(match.record_result, match.player_ids[1])
                tournament.scores[match.player_ids[1]] += 1
            elif result == "3":
                self.save_and_update(match.record_result, None)
                tournament.scores[match.player_ids[0]] += 0.5
                tournament.scores[match.player_ids[1]] += 0.5
            else:
                print("Invalid input. Skipping match.")
                continue

            match.completed = True
            self.results_view.confirm_result_entry(match)

        if tournament.current_round == tournament.total_rounds:
            if all(m.completed for m in round_obj.matches):
                tournament.completed = True
                print("Tournament is now complete!")
                self.display_rankings(tournament)
                self.tournament_service.save_tournaments()
                return

        self.display_rankings(tournament)
        self.tournament_service.save_tournaments()

    # This will display rankings
    def display_rankings(self, tournament):
        print("\nFinal Rankings:")
        rankings = tournament.get_rankings()
        for i, player in enumerate(rankings, start=1):
            print(f"{i}. {player.name} - {player.score} points")

    # This will users to move the tournament forward once results are entered.
    def advance_round(self, tournament):
        if tournament.completed:
            print("Tournament is already completed.")
            return

        current_round = tournament.current_round

        if current_round == 0:
            print("No rounds have started yet. Creating rounds now...")
            tournament.create_rounds()
            tournament.advance_round()
            print(f"Round {tournament.current_round} has started.")
            self.tournament_service.save_tournaments()
            return

        round_obj = tournament.rounds[current_round - 1]
        if any(not m.completed for m in round_obj.matches):
            print("Cannot advance. Some matches in the current round are incomplete.")
            return

        # Only advance if not already in final round
        if current_round < tournament.total_rounds:
            tournament.advance_round()
            print(f"Advanced to Round {tournament.current_round}.")
        else:
            print(
                "Final round is already active. Enter results to complete the tournament."
            )

        self.tournament_service.save_tournaments()

    # This will allow users to view final standings and match history once the tournament is complete.
    def generate_report(self, tournament):
        # Shows tournament metadata (name, venue, dates, etc.)
        print("\n*** Tournament Report ***")
        print(f"Name: {tournament.name}")
        print(f"Venue: {tournament.venue}")
        print(f"Dates: {tournament.dates.start_date} to {tournament.dates.end_date}")
        print(f"Total Rounds: {tournament.total_rounds}")
        print(f"Status: {'Completed' if tournament.completed else 'In Progress'}\n")

        # Displays final standings sorted by score
        print("🏆 Final Standings:")
        sorted_scores = tournament.get_sorted_scores()
        for rank, (chess_id, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {chess_id} — {score} pts")

        # Lists match results round by round
        print("\n📋 Match Results:")
        for round_obj in tournament.rounds:
            print(f"\nRound {round_obj.round_number}:")
            for match in round_obj.matches:
                p1, p2 = match.player_ids
                result = match.result
                if result is None:
                    outcome = "Draw"
                elif result == p1:
                    outcome = f"{p1} wins"
                elif result == p2:
                    outcome = f"{p2} wins"
                else:
                    outcome = "No result"
                print(f"{p1} vs {p2} → {outcome}")
