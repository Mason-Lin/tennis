from .tennis import TennisGame, Player
import pytest


@pytest.fixture
def game(player1, player2):
    game = TennisGame(player1, player2)
    return game


@pytest.fixture
def player1():
    return Player()


@pytest.fixture
def player2():
    return Player()
