from .tennis import TennisGame


def test_fifteen_love():
    game = TennisGame()
    game.first_player_score = 1
    assert game.first_player_score == 1


def test_fifteen_love():
    game = TennisGame()
    game.first_player_score = 1
    assert "Fifteen-Love" == game.score()



def test_fifteen_love():
    game = TennisGame()
    game.first_player_score = 2
    assert "Thirty-Love" == game.score()

