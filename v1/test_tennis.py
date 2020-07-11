from .tennis import TennisGame


def test_Love_All():
    game = TennisGame()
    score = game.Score()
    assert score == "Love All"


def test_fifteen_love():
    game = TennisGame()
    game.firstPlayerScore = 1
    score = game.Score()
    assert score == "Fifteen Love"


def test_thirty_love():
    game = TennisGame()
    game.firstPlayerScore = 2
    score = game.Score()
    assert score == "Thirty Love"


def test_forty_love():
    game = TennisGame()
    game.firstPlayerScore = 3
    score = game.Score()
    assert score == "Forty Love"
