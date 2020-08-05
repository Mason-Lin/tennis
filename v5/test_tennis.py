import pytest


def win_multiple_time(who, times):
    for _ in range(times):
        who.win_score()


def test_fifteen_love(game, player1, player2):
    win_multiple_time(player1, 1)
    win_multiple_time(player2, 0)
    assert game.score() == "Fifteen-Love"


def test_thirty_love(game, player1, player2):
    win_multiple_time(player1, 2)
    win_multiple_time(player2, 0)
    assert game.score() == "Thirty-Love"


def test_forty_love(game, player1, player2):
    win_multiple_time(player1, 3)
    win_multiple_time(player2, 0)
    assert game.score() == "Forty-Love"


def test_love_fifteen(game, player1, player2):
    win_multiple_time(player1, 0)
    win_multiple_time(player2, 1)
    assert game.score() == "Love-Fifteen"


def test_love_thirty(game, player1, player2):
    win_multiple_time(player1, 0)
    win_multiple_time(player2, 2)
    assert game.score() == "Love-Thirty"


def test_love_forty(game, player1, player2):
    win_multiple_time(player1, 0)
    win_multiple_time(player2, 3)
    assert game.score() == "Love-Forty"


def test_love_all(game, player1, player2):
    win_multiple_time(player1, 0)
    win_multiple_time(player2, 0)
    assert game.score() == "Love-All"