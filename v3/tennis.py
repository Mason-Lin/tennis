from enum import Enum


class Player():
    def __init__(self, name):
        self.score = 0
        self.name = name


class SCORE_LOOKUP(Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3


class TennisGame():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    @staticmethod
    def win_score(player):
        player.score += 1

    def score(self):
        ready_to_win = self.is_ready_to_win()
        return self.same_score(ready_to_win) if self.is_same_score() else self.diff_score(ready_to_win)

    def same_score(self, ready_to_win):
        return self.same_score_adv_result() if ready_to_win else self.same_score_normal_result()

    def diff_score(self, ready_to_win):
        return self.diff_score_adv_result() if ready_to_win else self.diff_score_normal_result()

    def diff_score_adv_result(self):
        return f"{self.get_winner()} {self.get_state()}"

    def diff_score_normal_result(self):
        return f"{SCORE_LOOKUP(self.player1.score).name}-{SCORE_LOOKUP(self.player2.score).name}"

    def same_score_adv_result(self):
        return "Deuce"

    def same_score_normal_result(self):
        return f"{SCORE_LOOKUP(self.player1.score).name}-All"

    def is_same_score(self):
        return self.player2.score == self.player1.score

    def is_ready_to_win(self):
        return min(self.player2.score, self.player1.score) >= 3

    def get_winner(self):
        return self.player1.name if self.player1.score > self.player2.score else self.player2.name

    def get_state(self):
        return "Win" if max(self.player2.score, self.player1.score) == 5 else "Adv"
