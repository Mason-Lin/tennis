class TennisGame():

    @property
    def first_player_score(self):
        return self._first_player_score

    @first_player_score.setter
    def first_player_score(self, score):
        self._first_player_score = score

    def score(self):
        if self.first_player_score == 1:
            return "Fifteen-Love"
        if self.first_player_score == 2:
            return "Thirty-Love"

# 