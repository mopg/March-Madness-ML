import numpy as np

from prediction import findWinner

MAPPING_ROUNDS = {
    'First Four': 'Round 1',
    'Round 1': 'Round 2',
    'Round 2': 'Sweet 16',
    'Sweet 16': 'Elite 8',
    'Elite 8': 'Final 4',
    'Final 4' : 'Championship game',
}

def increment_round_str(round_str):
    return MAPPING_ROUNDS[round_str]

class TournamentGame:

    def __init__(
        self,
        team_1 = None,
        team_2 = None,
        round_str = None,
    ):

        if isinstance(team_1, str):
            self.team_1 = team_1
        else:
            self.child_1 = team_1
            self.team_1 = None

        if isinstance(team_2, str):
            self.team_2 = team_2
        else:
            self.child_2 = team_2
            self.team_2 = None
        
        self.round_str = round_str

        if round_str is None:
            if self.team_1 is None:
                self.round_str = increment_round_str(self.child_1.round_str)
            if self.team_2 is None:
                self.round_str = increment_round_str(self.child_2.round_str)


    def predict_result(
        self,
        model,
    ):

        if self.team_1 is None:
            self.child_1.predict_result(model)
            self.team_1 = self.child_1.winning_team

        if self.team_2 is None:
            self.child_2.predict_result(model)
            self.team_2 = self.child_2.winning_team

        # Run prediction
        self.winning_team, prob = findWinner(self.team_1, self.team_2, model)

        prob_perc = prob * 100.0
        print(f"{self.round_str}: Between {self.team_1} and {self.team_2}, {self.winning_team} wins with {prob_perc:.1f}% probability")
