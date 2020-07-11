class TennisGame(object):

    @property
    def firstPlayerScore(self):
        return self._firstPlayerScore

    @firstPlayerScore.setter
    def firstPlayerScore(self, score):
        self._firstPlayerScore = score

    @property
    def secondPlayerScore(self):
        return self._secondPlayerScore

    @secondPlayerScore.setter
    def secondPlayerScore(self, score):
        self._secondPlayerScore = score

    @property
    def firstPlayerName(self):
        return self._firstPlayerName

    @firstPlayerName.setter
    def firstPlayerName(self, name):
        self._firstPlayerName = name

    @property
    def secondPlayerName(self):
        return self._secondPlayerName

    @secondPlayerName.setter
    def secondPlayerName(self, name):
        self._secondPlayerName = name

    def __init__(self):
        super().__init__()
        self.firstPlayerScore = 0
        self.secondPlayerScore = 0
        self.firstPlayerName = "Mason"
        self.secondPlayerName = "Rina"

    def Score(self):
        score_lookup = {
            "0": "Love",
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
        }

        if self.is_same_score():
            return "Deuce" if self.firstPlayerScore > 2 else f"{score_lookup[str(self.firstPlayerScore)]} All"

        if self.one_of_player_is_zero():
            return f"{score_lookup[str(self.firstPlayerScore)]} {score_lookup[str(self.secondPlayerScore)]}"

        if self.is_adv_state():
            return f"{self.get_winner()} {self.get_state()}"

    def one_of_player_is_zero(self):
        return self.firstPlayerScore == 0 or self.secondPlayerScore == 0

    def get_winner(self):
        return self.firstPlayerName if self.firstPlayerScore > self.secondPlayerScore else self.secondPlayerName

    def get_state(self):
        return "Adv" if max(self.firstPlayerScore, self.secondPlayerScore) == 4 else "Win"

    def is_adv_state(self):
        return sorted((self.firstPlayerScore, self.secondPlayerScore)) in [sorted((3, 4)), sorted((3, 5))]

    def is_same_score(self):
        return self.firstPlayerScore == self.secondPlayerScore
