from .tennis import TennisGame


def test_fifteen_love():
    game = TennisGame()
    game.first_player_score = 1
    assert game.first_player_score == 1


def test_fifteen_love():
    game = TennisGame()
    game.first_player_score = 1
    assert "Fifteen-Love" == game.score()



def test_thirty_love():
    game = TennisGame()
    game.first_player_score = 2
    assert "Thirty-Love" == game.score()


def test_forty_love():
    game = TennisGame()
    game.first_player_score = 3
    assert "Forty-Love" == game.score()


def test_thirty_love():
    game = TennisGame()
    game.second_player_score = 2
    assert "Love-Thirty" == game.score()


def test_love_forty():
    game = TennisGame()
    game.second_player_score = 3
    assert "Love-Forty" == game.score()



# 0-1 Love-Fifteen
# 0-2 Love-Thirty