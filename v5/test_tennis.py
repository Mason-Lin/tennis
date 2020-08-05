import pytest

from .tennis import TennisGame, Player


def test_fifteen_love():
    player1 = Player()
    player2 = Player()
    game = TennisGame(player1, player2)
    game.first_player_get_score()
    assert game.score() == "Fifteen-Love"


def test_thirty_love():
    player1 = Player()
    player2 = Player()
    game = TennisGame(player1, player2)
    game.first_player_get_score()
    game.first_player_get_score()
    assert game.score() == "Thirty-Love"
