class TennisGame(object):
    _firstPlayerScoreTimes = 0

    def Score(self):
        if self._firstPlayerScoreTimes:
            return "Fifteen Love"
        return "Love All"

    def FirstPlayerScore(self):
        self._firstPlayerScoreTimes += 1
