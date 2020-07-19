class TennisGame():
    def __init__(self):
        self._first_player_score = 0
    
    def first_player_score(self):
        self._first_player_score += 1

    def score(self):
        if self._first_player_score == 1:
            return "Fifteen-Love"