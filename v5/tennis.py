import enum


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

    def is_ready_to_win(self):
        return (
            min(self.player1.get_score(), self.player2.get_score())
            >= SCORE_LOOKUP.Forty.value
        )

    def get_winner(self):
        return (
            self.player1
            if self.player1.get_score() > self.player2.get_score()
            else self.player2
        )

    def is_same_score(self):
        return self.player1.get_score() == self.player2.get_score()

    def get_return_format(self):
        return {
            (0, 0): "{score1}-{score2}",
            (0, 1): "{winner_name} {winner_score}",
            (1, 0): "{score1}-All",
            (1, 1): "Deuce",
        }[(self.is_same_score(), self.is_ready_to_win())]

    def get_return_metadata(self):
        score1 = SCORE_LOOKUP(self.player1.get_score()).name
        score2 = SCORE_LOOKUP(self.player2.get_score()).name
        winner = self.get_winner()
        return {
            "score1": score1,
            "score2": score2,
            "winner_name": winner.get_name(),
            "winner_score": SCORE_LOOKUP(winner.get_score()).name,
        }

    def score(self):
        return self.get_return_format().format(**self.get_return_metadata())
