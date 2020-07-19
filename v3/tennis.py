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
                winner = self._first_player_name if self._first_player_score > self._second_player_score else self._second_player_name
                state = " Win" if max(self._second_player_score, self._first_player_score) == 5 else " Adv"
                if self._first_player_score > self._second_player_score:
                    if self._first_player_score > 4:
                        return winner + state
                    return winner + state
                else:
                    if self._second_player_score > 4:
                        return winner + state
                    return winner + state
            else:
                return score_lookup[str(self._first_player_score)] + "-" + score_lookup[str(self._second_player_score)]
