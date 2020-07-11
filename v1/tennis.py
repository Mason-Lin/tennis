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

    def __init__(self):
        super().__init__()
        self.firstPlayerScore = 0
        self.secondPlayerScore = 0

    def Score(self):
        score_lookup = {
            "0": "Love",
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
        }

        if self.firstPlayerScore or self.secondPlayerScore:
            if self.firstPlayerScore == self.secondPlayerScore:
                if self.firstPlayerScore > 2:
                    return "Deuce"
                else:
                    return f"{score_lookup[str(self.firstPlayerScore)]} All"
            return f"{score_lookup[str(self.firstPlayerScore)]} {score_lookup[str(self.secondPlayerScore)]}"
        else:
            return "Love All"
