class TennisGame():

    @property
    def first_player_score(self):
        return self._first_player_score

    @first_player_score.setter
    def first_player_score(self, score):
        self._first_player_score = score

    def score(self):
        score_lookup = {
            "1": "Fifteen-Love",
            "2": "Thirty-Love",
            "3": "Forty-Love"
        }
        if self.first_player_score in (1, 2, 3):
            return score_lookup[str(self.first_player_score)]

# Forty-Love
#
