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


def test_love_fifteen():
    game = TennisGame()
    game.secondPlayerScore = 1
    score = game.Score()
    assert score == "Love Fifteen"


def test_love_thirty():
    game = TennisGame()
    game.secondPlayerScore = 2
    score = game.Score()
    assert score == "Love Thirty"


def test_love_forty():
    game = TennisGame()
    game.secondPlayerScore = 3
    score = game.Score()
    assert score == "Love Forty"


def test_fifteen_love():
    game = TennisGame()
    game.firstPlayerScore = 1
    game.secondPlayerScore = 1
    score = game.Score()
    assert score == "Fifteen Love"



# 0-0 Love-All
# 1-1 Fifteen-All
# 2-2 Thirty-All