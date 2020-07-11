class TennisGame(object):
    _firstPlayerScoreTimes = 0

    def Score(self):
        score_lookup = {
            "1": "Fifteen Love",
            "2": "Thirty Love",
            "3": "Forty Love"
        }
        if self._firstPlayerScoreTimes:
            return score_lookup[str(self._firstPlayerScoreTimes)]
        return "Love All"

    def FirstPlayerScore(self):
        self._firstPlayerScoreTimes += 1
