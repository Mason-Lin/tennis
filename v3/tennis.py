class TennisGame():
    def __init__(self):
        self._first_player_score = 0

    def first_player_score(self):
        self._first_player_score += 1

    def score(self):
        score_lookup = {
            "1": "Fifteen-Love",
            "2": "Thirty-Love",
            "3": "Forty-Love"
        }
        return score_lookup[str(self._first_player_score)]
        # if self._first_player_score == 1:
        #     return "Fifteen-Love"
        # elif self._first_player_score == 2:
        #     return "Thirty-Love"
