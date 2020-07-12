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


def test_love_fifteen():
    game = TennisGame()
    game.second_player_score = 1
    assert "Love-Fifteen" == game.score()


def test_love_thirty():
    game = TennisGame()
    game.second_player_score = 2
    assert "Love-Thirty" == game.score()


def test_love_forty():
    game = TennisGame()
    game.second_player_score = 3
    assert "Love-Forty" == game.score()


def test_love_all():
    game = TennisGame()
    game.first_player_score = 0
    game.second_player_score = 0
    assert "Love-All" == game.score()


def test_fifteen_all():
    game = TennisGame()
    game.first_player_score = 1
    game.second_player_score = 1
    assert "Fifteen-All" == game.score()


def test_thirty_all():
    game = TennisGame()
    game.first_player_score = 2
    game.second_player_score = 2
    assert "Thirty-All" == game.score()


def test_forty_deuce():
    game = TennisGame()
    game.first_player_score = 3
    game.second_player_score = 3
    assert "Deuce" == game.score()


def test_deuce():
    game = TennisGame()
    game.first_player_score = 4
    game.second_player_score = 4
    assert "Deuce" == game.score()


def test_first_adv():
    game = TennisGame("Mason", "Rina")
    game.first_player_score = 4
    game.second_player_score = 3
    assert "Mason Adv" == game.score()


def test_second_adv():
    game = TennisGame("Mason", "Rina")
    game.first_player_score = 3
    game.second_player_score = 4
    assert "Rina Adv" == game.score()


def test_first_win():
    game = TennisGame("Mason", "Rina")
    game.first_player_score = 5
    game.second_player_score = 3
    assert "Mason Win" == game.score()


def test_second_win():
    game = TennisGame("Mason", "Rina")
    game.first_player_score = 3
    game.second_player_score = 5
    assert "Rina Win" == game.score()
