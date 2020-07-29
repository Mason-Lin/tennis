from .tennis import TennisGame


def win_multiple_score(who, times):
    for _ in range(times):
        who.win_score()


def test_fifteen_love(game, player1):
    win_multiple_score(player1, 1)
    assert game.score() == "Fifteen-Love"


def test_thirty_love(game, player1):
    win_multiple_score(player1, 2)
    assert game.score() == "Thirty-Love"


def test_forty_love(game, player1):
    win_multiple_score(player1, 3)
    assert game.score() == "Forty-Love"


def test_love_fifteen(game, player2):
    win_multiple_score(player2, 1)
    assert game.score() == "Love-Fifteen"


def test_love_thirty(game, player2):
    win_multiple_score(player2, 2)
    assert game.score() == "Love-Thirty"


def test_love_forty(game, player2):
    win_multiple_score(player2, 3)
    assert game.score() == "Love-Forty"


def test_love_all(game):
    assert game.score() == "Love-All"


def test_love_11(game, player1, player2):
    win_multiple_score(player1, 1)
    win_multiple_score(player2, 1)
    assert game.score() == "Fifteen-All"


def test_love_22(game, player1, player2):
    win_multiple_score(player1, 2)
    win_multiple_score(player2, 2)
    assert game.score() == "Thirty-All"


def test_love_33(game, player1, player2):
    win_multiple_score(player1, 3)
    win_multiple_score(player2, 3)
    assert game.score() == "Deuce"


def test_love_44(game, player1, player2):
    win_multiple_score(player1, 4)
    win_multiple_score(player2, 4)
    assert game.score() == "Deuce"


def test_43(game, player1, player2):
    win_multiple_score(player1, 4)
    win_multiple_score(player2, 3)
    assert game.score() == "Mason Adv"


def test_53(game, player1, player2):
    win_multiple_score(player1, 5)
    win_multiple_score(player2, 3)
    assert game.score() == "Mason Win"


def test_34(game, player1, player2):
    win_multiple_score(player1, 3)
    win_multiple_score(player2, 4)
    assert game.score() == "Rina Adv"


def test_35(game, player1, player2):
    win_multiple_score(player1, 3)
    win_multiple_score(player2, 5)
    assert game.score() == "Rina Win"
