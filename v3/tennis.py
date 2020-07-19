class TennisGame():
    def __init__(self):
        self._first_player_score = 0
        self._second_player_score = 0

    def first_player_score(self):
        self._first_player_score += 1

    def second_player_score(self):
        self._second_player_score += 1

    def score(self):
        score_lookup = {
            "0": "Love",
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
        }
        if self._second_player_score == self._first_player_score:
            if max(self._second_player_score, self._first_player_score) >= 3:
                return "Deuce"
            return score_lookup[str(self._first_player_score)] + "-All"
        else:
            return score_lookup[str(self._first_player_score)] + "-" + score_lookup[str(self._second_player_score)]
