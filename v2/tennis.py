class TennisGame():

    def __init__(self, first_player_name="player1", second_player_name="player2"):
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
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
            "0": "Love",
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
        }

        #  same
        if self.first_player_score == self.second_player_score:
            return "Deuce" if self.first_player_score in (3, 4) else f"{score_lookup[str(self.first_player_score)]}-All"

        # diff
        if self.first_player_score == 4 and self.second_player_score == 3:
            return f"{self.first_player_name} Adv"
        elif self.first_player_score == 5 and self.second_player_score == 3:
            return f"{self.first_player_name} Win"
        elif self.first_player_score == 3 and self.second_player_score == 4:
            return f"{self.second_player_name} Adv"


        if self.first_player_score in (1, 2, 3) or self.second_player_score in (1, 2, 3):

            return f"{score_lookup[str(self.first_player_score)]}-{score_lookup[str(self.second_player_score)]}"
