# PlayerService supports player registration, search, and retrieval across clubs. 
# This service will be used by the controller when registering players to a tournament.
class PlayerService:
    def __init__(self, club_manager):
        self.club_manager = club_manager

    #Returns all players across all clubs
    def get_all_players(self):
        players = []
        for club in self.club_manager.clubs:
            players.extend(club.players)
        return players

    # Finds a player by their unique ID
    def search_by_chess_id(self, chess_id):
        for player in self.get_all_players():
            if player.chess_id == chess_id:
                return player
        return None

    # Case-insensitive search by partial name
    def search_by_name(self, name_fragment):
        name_fragment = name_fragment.lower()
        return [
            player for player in self.get_all_players()
            if name_fragment in player.name.lower()
        ]