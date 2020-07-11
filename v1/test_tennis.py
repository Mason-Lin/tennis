from .tennis import TennisGame


def test_Love_All():
    game = TennisGame()
    score = game.Score()
    assert score == "Love All"


def test_fifteen_love():
    game = TennisGame()
    game.FirstPlayerScore()
    score = game.Score()
    assert score == "Fifteen Love"


def test_thirty_love():
    game = TennisGame()
    game.FirstPlayerScore()
    game.FirstPlayerScore()
    score = game.Score()
    assert score == "Thirty Love"
