from .tennis import TennisGame


def test_fifteen_love():
    game = TennisGame()
    game.firstPlayerScore = 1
    assert game.Score() == "Fifteen Love"


def test_thirty_love():
    game = TennisGame()
    game.firstPlayerScore = 2
    assert game.Score() == "Thirty Love"


def test_forty_love():
    game = TennisGame()
    game.firstPlayerScore = 3
    assert game.Score() == "Forty Love"


def test_love_fifteen():
    game = TennisGame()
    game.secondPlayerScore = 1
    assert game.Score() == "Love Fifteen"


def test_love_thirty():
    game = TennisGame()
    game.secondPlayerScore = 2
    assert game.Score() == "Love Thirty"


def test_love_forty():
    game = TennisGame()
    game.secondPlayerScore = 3
    assert game.Score() == "Love Forty"


def test_Love_All():
    game = TennisGame()
    assert game.Score() == "Love All"


def test_fifteen_love():
    game = TennisGame()
    game.firstPlayerScore = 1
    game.secondPlayerScore = 1
    assert game.Score() == "Fifteen All"


def test_thirty_love():
    game = TennisGame()
    game.firstPlayerScore = 2
    game.secondPlayerScore = 2
    assert game.Score() == "Thirty All"


def test_deuce_when_3_3():
    game = TennisGame()
    game.firstPlayerScore = 3
    game.secondPlayerScore = 3
    assert game.Score() == "Deuce"


def test_deuce_when_4_4():
    game = TennisGame()
    game.firstPlayerScore = 4
    game.secondPlayerScore = 4
    assert game.Score() == "Deuce"


def test_first_player_adv():
    game = TennisGame()
    game.firstPlayerScore = 4
    game.secondPlayerScore = 3
    assert game.Score() == "Mason Adv"


def test_second_player_adv():
    game = TennisGame()
    game.firstPlayerScore = 3
    game.secondPlayerScore = 4
    assert game.Score() == "Rina Adv"
