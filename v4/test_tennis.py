import pytest
from .tennis import TennisGame


def win_multiple_score(who, times):
    for _ in range(times):
        who.win_score()


TEST_DATA = [
    (1, 0, "Fifteen-Love"),
    (2, 0, "Thirty-Love"),
    (3, 0, "Forty-Love"),
    (0, 1, "Love-Fifteen"),
    (0, 2, "Love-Thirty"),
    (0, 3, "Love-Forty"),
    (0, 0, "Love-All"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    (3, 3, "Deuce"),
    (4, 4, "Deuce"),
    (4, 3, "Mason Adv"),
    (5, 3, "Mason Win"),
    (3, 4, "Rina Adv"),
    (3, 5, "Rina Win"),
]


@pytest.mark.parametrize("score1, score2, result", TEST_DATA)
def test_score(game, player1, player2, score1, score2, result):
    win_multiple_score(player1, score1)
    win_multiple_score(player2, score2)
    assert game.score() == result
