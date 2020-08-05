import pytest

def test_fifteen_love():
    game = TennisGame()
    game.first_player_get_score()
    assert game.score() == "Fifteen-Love"
