from models.match import Match

# This class holds all the matches for a round
class Round:
    def __init__(self, round_number):
        self.round_number = round_number # identifies which round (1,2,3,4)
        self.matches = []  # list of Match objects (each is a game between players)

    # This function adds a new match to the round
    # ...and will be called when pairing players for that round
    def add_match(self, match: Match):
        self.matches.append(match)