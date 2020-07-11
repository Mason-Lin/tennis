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

        if self.firstPlayerScore or self.secondPlayerScore:
            if sorted((self.firstPlayerScore, self.secondPlayerScore)) == sorted((3, 4)):
                return f"{self.firstPlayerName} Adv" if self.firstPlayerScore > self.secondPlayerScore else f"{self.secondPlayerName} Adv"
            elif sorted((self.firstPlayerScore, self.secondPlayerScore)) == sorted((3, 5)):
                return f"{self.firstPlayerName} Win" if self.firstPlayerScore > self.secondPlayerScore else f"{self.secondPlayerName} Win"
            else:
                return f"{score_lookup[str(self.firstPlayerScore)]} {score_lookup[str(self.secondPlayerScore)]}"

    def is_same_score(self):
        return self.firstPlayerScore == self.secondPlayerScore
