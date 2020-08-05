import logging


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def win_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_lookup = {
            "0": "Love",
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty",
        }

    def is_going_to_win(self):
        return min(self.player1.get_score(), self.player2.get_score()) >= 3

    def get_status(self, player):
        return "Adv" if player.get_score() == 4 else "Win"

    def get_winner(self):
        return self.player1 if self.player1.get_score() > self.player2.get_score() else self.player2

    def score(self):
        logging.debug(self.player1.get_score)
        if self.player1.get_score() != self.player2.get_score():
            if self.is_going_to_win():
                winner = self.get_winner()
                return "{} {}".format(
                    winner.get_name(),
                    self.get_status(winner),
                )
            else:
                return "{}-{}".format(
                    self.score_lookup[str(self.player1.get_score())],
                    self.score_lookup[str(self.player2.get_score())],
                )
        else:
            # self.player1.get_score() == self.player2.get_score():
            if self.is_going_to_win():
                return "Deuce"
            else:
                return "{}-{}".format(
                    self.score_lookup[str(self.player1.get_score())],
                    "All",
                )
