
# This class represents a single game between two players during a round of a tournament.

class Match:
    def __init__(self, player_ids):
        self.player_ids = player_ids  # list of IDs for 2 players
        self.completed = False  # checks if match has been played
        self.winner_id = None  # player ID or None for draw
        self.result = None

    def record_result(self, winner_id):
        self.winner_id = winner_id # stores winning player's ID
        self.completed = True  # sets match to completed
        self.result = winner_id

    def to_dict(self):
        return {
            "player_ids": self.player_ids,
            "result": self.result,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        match = cls(player_ids=data["player_ids"])
        match.result = data["result"]
        match.completed = data["completed"]
        return match