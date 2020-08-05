import enum
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


class SCORE_LOOKUP(enum.Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3
    Adv = 4
    Win = 5


class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def is_going_to_win(self):
        return min(self.player1.get_score(), self.player2.get_score()) >= 3

    def get_winner(self):
        return (
            self.player1
            if self.player1.get_score() > self.player2.get_score()
            else self.player2
        )

    def is_same_score(self):
        return self.player1.get_score() == self.player2.get_score()

    def score(self):
        logging.debug(self.player1.get_score)
        if self.is_same_score():
            if self.is_going_to_win():
                return "Deuce"
            else:
                return "{}-{}".format(
                    SCORE_LOOKUP(self.player1.get_score()).name, "All"
                )
        else:
            if self.is_going_to_win():
                winner = self.get_winner()
                return "{} {}".format(
                    winner.get_name(), SCORE_LOOKUP(winner.get_score()).name,
                )
            else:
                return "{}-{}".format(
                    SCORE_LOOKUP(self.player1.get_score()).name,
                    SCORE_LOOKUP(self.player2.get_score()).name,
                )
