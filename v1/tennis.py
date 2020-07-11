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

        if self.firstPlayerScore or self.secondPlayerScore:
            if self.firstPlayerScore == self.secondPlayerScore:
                if self.firstPlayerScore > 2:
                    return "Deuce"
                else:
                    return f"{score_lookup[str(self.firstPlayerScore)]} All"
            elif (self.firstPlayerScore, self.secondPlayerScore) == (4, 3):
                return f"{self.firstPlayerName} Adv"
            return f"{score_lookup[str(self.firstPlayerScore)]} {score_lookup[str(self.secondPlayerScore)]}"
        else:
            return "Love All"
