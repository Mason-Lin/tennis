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
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
        }
        if self.firstPlayerScore:
            return score_lookup[str(self.firstPlayerScore)] + " Love"
        elif self.secondPlayerScore:
            return "Love " + score_lookup[str(self.secondPlayerScore)]
        else:
            return "Love All"
