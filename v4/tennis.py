import enum


class Player():
    def __init__(self, name):
        self.score = 0
        self.name = name

    def win_score(self):
        self.score += 1


class SCORE_LOOKUP(enum.Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3
    Adv = 4
    Win = 5


class TennisGame():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def score(self):
        return self.get_output_format().format(**self.get_output_data())

    def get_output_format(self):
        return {
            (True, True): "{state}",
            (True, False): "{score1}-All",
            (False, True): "{winner} {state}",
            (False, False): "{score1}-{score2}"
        }[(self.is_same_score(), self.is_ready_to_win())]

    def get_output_data(self):
        return {
            "score1": SCORE_LOOKUP(self.player1.score).name,
            "score2": SCORE_LOOKUP(self.player2.score).name,
            "winner": self.get_winner(),
            "state": self.get_adv_state()
        }

    def get_winner(self):
        return self.player1.name if self.player1.score > self.player2.score else self.player2.name

    def get_adv_state(self):
        return "Deuce" if self.is_same_score() else SCORE_LOOKUP(max(self.player1.score, self.player2.score)).name

    def is_same_score(self):
        return self.player1.score == self.player2.score

    def is_ready_to_win(self):
        return min(self.player1.score, self.player2.score) >= SCORE_LOOKUP.Forty.value
