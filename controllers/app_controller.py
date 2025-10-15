from views.main_screen_view import MainScreenView
from views.manage_tournament_view import ManageTournamentView
from models.tournament import Tournament
from services.tournament_service import TournamentService
from services.player_service import PlayerService

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
        self.player_service = PlayerService()
        self.main_view = MainScreenView()
        self.manage_view = ManageTournamentView()

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
        tournaments = self.tournament_service.get_all_tournaments()

        if not tournaments:
            self.main_view.display_no_tournaments_message()
            selection = 'new'
        else:
            self.main_view.display_tournament_list(tournaments)
            selection = self.main_view.prompt_tournament_selection()

        if selection.lower() == 'new':
            tournament = self.tournament_service.create_tournament()
            self.manage_tournament(tournament)
        else:
            try:
                index = int(selection) - 1
                tournament = tournaments[index]
                self.manage_tournament(tournament)
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
                self.show_main_screen()

    # Displays tournament details and options
    def manage_tournament(self, tournament):
        self.manage_view.display_tournament_details(tournament)
        self.manage_view.display_manage_options()
        choice = self.manage_view.prompt_manage_choice()

        # Placeholder for routing logic
        print(f"You selected option {choice}. Routing not yet implemented.")