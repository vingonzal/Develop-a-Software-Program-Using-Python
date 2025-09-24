from models.dates import Dates
from models.round import Round


class Tournament:

    def __init__(self, name, venue, dates : Dates, registered_players, total_rounds, current_round):
        self.name = name
        self.venue = venue
        self.dates = dates
        self.registered_players = registered_players 
        self.rounds = [] # list of Round objects that contain matches
        self.total_rounds = total_rounds
        self.current_round = 0 #index to keep track of active round
        self.completed = False

    # advance to next round
    def advance_round(self):
        # check to see if tournament is stll going and keeps track
        if self.current_round < self.total_rounds:
            # if so move to next round
            self.current_round += 1
        else:
            # if all rounds are done, mark True so app knows tournament is finished
            self.completed = True
