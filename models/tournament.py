import random # required for the shuffle() function
from models.dates import Dates
from models.match import Match
from models.player import Player
from models.round import Round

# This class serves as the conductor
class Tournament:

    def __init__(self, name, venue, dates : Dates, registered_players, total_rounds):
        self.name = name
        self.venue = venue
        self.dates = dates
        self.registered_players = registered_players 
        self.rounds = [] # list of Round objects that contain matches
        self.total_rounds = total_rounds
        self.current_round = 0 #index to keep track of active round
        self.completed = False
        self.scores = {player.chess_id: 0 for player in registered_players}

    # Method to register play dynamically - this will support the register player screen
    def register_player(self, player):
        if player not in self.registered_players:
            self.registered_players.append(player)
            self.scores[player.chess_id] = 0

    # advance to next round
    def advance_round(self):
        # check to see if tournament is stll going and keeps track
        if self.current_round < self.total_rounds:
            # if so move to next round
            self.current_round += 1
        else:
            # if all rounds are done, mark True so app knows tournament is finished
            self.completed = True
    
    # Method to sort scores
    def get_sorted_scores(self):
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

    # This method builds all rounds and matches...
    # ... looping through the total number of rounds and building them automatically using _create_round().
    def create_rounds(self):
        for round_number in range(1, self.total_rounds + 1): # start at 1 and include round 4
            round_object = self._create_round(round_number)
            self.rounds.append(round_object)

    # This private method creates a single round and fills it with matches between randomly paired players.
    # Ensure players are shuffled before pairing
    def _create_round(self, round_number):
        # - Make a copy of the list of registered player IDs,
        # ...so the list can be shuffled without affecting the original order stored in the tournament.
        players = self.registered_players.copy()
        random.shuffle(players) # Randomize the order of players
        matches = [] # Initialize an empty list to hold the match objects for this round.
        # Loop through the shuffled player list two at a time
        for i in range(0, len(players), 2):
            pair = players[i:i+2] #slice out two players at a time from list
            if len(pair) == 2: #avoids creating match with only 1 player
                match = self._create_match(pair)
                matches.append(match)
        # create new round object and assign current round #
        round_object = Round(round_number)
        for match in matches:
            round_object.add_match(match) #adds each match to the round
        return round_object #fully constructed round
    
    # This private method creates a match between two players.
    def _create_match(self, player_ids):
        return Match(player_ids)

    # This method randomly assign results to all matches in all rounds.
    def complete_tournament(self):
        # Outter loop ensures every round is processed
        for round_object in self.rounds:
            # Inner loop targets each individual game
            for match in round_object.matches:
                # randomly picks a number; stimulates match outcome without needing user input
                result = random.choice([0, 1, 2])  # 0 = draw, 1 = player 1 wins, 2 = player 2 wins
                # track and update scores
                if result == 0:
                    match.record_result(None)  # draw
                    self.scores[match.player_ids[0]] += 0.5
                    self.scores[match.player_ids[1]] += 0.5
                elif result == 1:
                    match.record_result(match.player_ids[0])
                    self.scores[match.player_ids[0]] += 1
                elif result == 2:
                    match.record_result(match.player_ids[1])
                    self.scores[match.player_ids[0]] += 1
        #mark tournament as finished
        self.completed = True

    # Method to check tournament status
    def is_active(self):
        return not self.completed