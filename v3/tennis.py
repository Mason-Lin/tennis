class TennisGame():
    def __init__(self, name1, name2):
        self._first_player_score = 0
        self._second_player_score = 0
        self._first_player_name = name1
        self._second_player_name = name2

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
        # 4 3 
        if self._second_player_score == self._first_player_score:
            if max(self._second_player_score, self._first_player_score) >= 3:
                return "Deuce"
            return score_lookup[str(self._first_player_score)] + "-All"
        else:
            if min(self._second_player_score, self._first_player_score) >= 3:
                return f"{self.get_winner()} {self.get_state()}"
            else:
                return score_lookup[str(self._first_player_score)] + "-" + score_lookup[str(self._second_player_score)]

    def get_winner(self):
        return self._first_player_name if self._first_player_score > self._second_player_score else self._second_player_name

    def get_state(self):
        return "Win" if max(self._second_player_score, self._first_player_score) == 5 else "Adv"
