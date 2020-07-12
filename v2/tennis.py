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
        self.score_lookup = {
            "0": "Love",
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty",
            "4": "Adv",
            "5": "Win"
        }

        if self.is_same_score():
            return self.get_high_same_score_result() if self.is_both_score_high_than_forty() else self.get_low_same_score_result()
        else:
            return self.get_high_diff_score_result() if self.is_both_score_high_than_forty() else self.get_low_diff_score_result()

    def get_low_same_score_result(self):
        return f"{self.score_lookup[str(self.first_player_score)]}-All"

    def get_low_diff_score_result(self):
        return f"{self.score_lookup[str(self.first_player_score)]}-{self.score_lookup[str(self.second_player_score)]}"

    def get_high_same_score_result(self):
        return "Deuce"

    def get_high_diff_score_result(self):
        return f"{self.get_winner()} {self.get_adv_statue_by_max_score()}"

    def get_winner(self):
        return self.first_player_name if self.first_player_score > self.second_player_score else self.second_player_name

    def get_adv_statue_by_max_score(self):
        return self.score_lookup[str(max(self.first_player_score, self.second_player_score))]

    def is_both_score_high_than_forty(self):
        return min(self.first_player_score, self.second_player_score) >= 3

    def is_same_score(self):
        return self.first_player_score == self.second_player_score
