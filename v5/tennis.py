import logging


class Player:
    def __init__(self):
        self.score = 0

    def win_score(self):
        self.score += 1

    def get_score(self):
        return self.score

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_lookup = {"0": "Love", "1": "Fifteen", "2": "Thirty", "3": "Forty"}

    def score(self):
        logging.debug(self.player1.get_score)
        if self.player1.get_score() != self.player2.get_score():
            return "{}-{}".format(
                self.score_lookup[str(self.player1.get_score())],
                self.score_lookup[str(self.player2.get_score())],
            )
        else:
            raise NotImplementedError
