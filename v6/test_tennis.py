import logging
import pytest


from .tennis import TennisGame, Player


def test_player_should_have_a_name():
    with pytest.raises(TypeError):
        Player()


def test_player_get_name_should_be_match():
    player = Player("Mason")
    assert player.get_name() == "Mason"


def test_player_get_score_default_should_be_zero():
    player = Player("Mason")
    assert player.get_score() == 0


def test_player_win_score():
    player = Player("Mason")
    player.win_score()
    assert player.score == 1


def test_tennis_needs_two_players():
    with pytest.raises(TypeError):
        TennisGame()


@pytest.mark.parametrize(
    "score1, score2, result",
    [
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
    ],
)
def test_tennis_score(monkeypatch, score1, score2, result):
    player1 = Player("Mason")
    player2 = Player("Rina")
    monkeypatch.setattr(player1, "get_score", lambda: score1)
    monkeypatch.setattr(player2, "get_score", lambda: score2)

    game = TennisGame(player1, player2)
    assert game.score() == result


@pytest.mark.parametrize(
    "score1, score2, result",
    [
        (1, 0, False),
        (2, 0, False),
        (3, 0, False),
        (0, 1, False),
        (0, 2, False),
        (0, 3, False),
        (0, 0, False),
        (1, 1, False),
        (2, 2, False),
        (3, 3, True),
        (4, 4, True),
        (4, 3, True),
        (5, 3, True),
        (3, 4, True),
        (3, 5, True),
    ],
)
def test_tennis_score_at_least_forty(monkeypatch, score1, score2, result):
    player1 = Player("Mason")
    player2 = Player("Rina")
    monkeypatch.setattr(player1, "get_score", lambda: score1)
    monkeypatch.setattr(player2, "get_score", lambda: score2)

    game = TennisGame(player1, player2)
    assert game.score_at_least_forty() == result


@pytest.mark.parametrize(
    "score1, score2, result",
    [
        (1, 0, "Mason"),
        (2, 0, "Mason"),
        (3, 0, "Mason"),
        (0, 1, "Rina"),
        (0, 2, "Rina"),
        (0, 3, "Rina"),
        (4, 3, "Mason"),
        (5, 3, "Mason"),
        (3, 4, "Rina"),
        (3, 5, "Rina"),
    ],
)
def test_tennis_get_winner_when_score_different(
    monkeypatch, score1, score2, result
):
    player1 = Player("Mason")
    player2 = Player("Rina")
    monkeypatch.setattr(player1, "get_score", lambda: score1)
    monkeypatch.setattr(player2, "get_score", lambda: score2)

    game = TennisGame(player1, player2)
    assert game.get_winner().name == result


@pytest.mark.parametrize(
    "score1, score2, result",
    [(0, 0, None), (1, 1, None), (2, 2, None), (3, 3, None), (4, 4, None),],
)
def test_tennis_get_winner_when_score_same(monkeypatch, score1, score2, result):
    player1 = Player("Mason")
    player2 = Player("Rina")
    monkeypatch.setattr(player1, "get_score", lambda: score1)
    monkeypatch.setattr(player2, "get_score", lambda: score2)

    game = TennisGame(player1, player2)
    assert game.get_winner() == result
