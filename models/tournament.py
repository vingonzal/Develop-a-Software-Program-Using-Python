from models.dates import Dates

class Tournament:

    def __init__(self, name, venue, dates : Dates, registered_players, number_of_rounds, current_round):
        self.name = name
        self.venue = venue
        self.dates = dates
        self.registered_players = registered_players 
        self.rounds = [] 
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.completed = False
