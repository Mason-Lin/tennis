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
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
        }
        if self._second_player_score == 0:
            return score_lookup[str(self._first_player_score)] + "-Love"

        if self._first_player_score == 0:
            return "Love-" + score_lookup[str(self._second_player_score)]
