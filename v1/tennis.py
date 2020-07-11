class TennisGame(object):
    _firstPlayerScoreTimes = 0

    def Score(self):
        if self._firstPlayerScoreTimes == 1:
            return "Fifteen Love"
        elif self._firstPlayerScoreTimes == 2:
            return "Thirty Love"
        return "Love All"

    def FirstPlayerScore(self):
        self._firstPlayerScoreTimes += 1
