from .tennis import TennisGame


def test_fifteen_love(game):
    game.first_player_score()
    assert game.score() == "Fifteen-Love"


def test_thirty_love(game):
    game.first_player_score()
    game.first_player_score()
    assert game.score() == "Thirty-Love"


def test_thirty_love(game):
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    assert game.score() == "Forty-Love"
