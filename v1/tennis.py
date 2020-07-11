class TennisGame(object):

    @property
    def firstPlayerScore(self):
        return self._firstPlayerScore

    @firstPlayerScore.setter
    def firstPlayerScore(self, score):
        self._firstPlayerScore = score

    def __init__(self):
        super().__init__()
        self.firstPlayerScore = 0

    def Score(self):
        score_lookup = {
            "1": "Fifteen Love",
            "2": "Thirty Love",
            "3": "Forty Love"
        }
        if self.firstPlayerScore:
            return score_lookup[str(self.firstPlayerScore)]
        return "Love All"
