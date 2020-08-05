import pytest

from .tennis import TennisGame, Player

def win_multiple_time(who, times):
    for _ in range(times):
        who.win_score()

def test_fifteen_love():
    player1 = Player()
    player2 = Player()
    game = TennisGame(player1, player2)
    win_multiple_time(player1, 1)
    win_multiple_time(player2, 0)
    assert game.score() == "Fifteen-Love"


def test_thirty_love():
    player1 = Player()
    player2 = Player()
    game = TennisGame(player1, player2)
    win_multiple_time(player1, 2)
    win_multiple_time(player2, 0)
    assert game.score() == "Thirty-Love"


def test_forty_love():
    player1 = Player()
    player2 = Player()
    game = TennisGame(player1, player2)
    win_multiple_time(player1, 3)
    win_multiple_time(player2, 0)
    assert game.score() == "Forty-Love"


def test_love_fifteen():
    player1 = Player()
    player2 = Player()
    game = TennisGame(player1, player2)
    win_multiple_time(player1, 0)
    win_multiple_time(player2, 1)
    assert game.score() == "Love-Fifteen"
