from .tennis import TennisGame, Player
import pytest


@pytest.fixture
def game(player1, player2):
    return TennisGame(player1, player2)


@pytest.fixture
def player1():
    return Player()


@pytest.fixture
def player2():
    return Player()
