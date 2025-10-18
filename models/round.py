from models.match import Match


# This class holds all the matches for a round
class Round:
    def __init__(self, round_number):
        self.round_number = round_number  # identifies which round (1,2,3,4)
        self.matches = []  # list of Match objects (each is a game between players)

    # This function adds a new match to the round
    # ...and will be called when pairing players for that round
    def add_match(self, match: Match):
        self.matches.append(match)

    def to_dict(self):
        return {
            "round_number": self.round_number,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, data):
        round_obj = cls(round_number=data["round_number"])
        round_obj.matches = [Match.from_dict(m) for m in data["matches"]]
        return round_obj
