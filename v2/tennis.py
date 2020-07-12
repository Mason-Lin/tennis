class TennisGame():

    def __init__(self):
        self.first_player_score = 0
        self.second_player_score = 0

    @property
    def first_player_score(self):
        return self._first_player_score

    @first_player_score.setter
    def first_player_score(self, score):
        self._first_player_score = score

    @property
    def second_player_score(self):
        return self._second_player_score

    @second_player_score.setter
    def second_player_score(self, score):
        self._second_player_score = score


    def score(self):
        score_lookup = {
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
        }

        if self.first_player_score in (1, 2, 3):
            return f"{score_lookup[str(self.first_player_score)]}-Love"

        if self.second_player_score == 3:
            return f"Love-{score_lookup[str(self.second_player_score)]}"


# Forty-Love
#
