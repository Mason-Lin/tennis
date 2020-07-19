from .tennis import TennisGame


def test_fifteen_love(game):
    game.first_player_score()
    assert game.score() == "Fifteen-Love"


def test_thirty_love(game):
    game.first_player_score()
    game.first_player_score()
    assert game.score() == "Thirty-Love"


def test_thirty_love(game):
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    assert game.score() == "Forty-Love"


def test_love_fifteen(game):
    game.second_player_score()
    assert game.score() == "Love-Fifteen"


def test_love_thirty(game):
    game.second_player_score()
    game.second_player_score()
    assert game.score() == "Love-Thirty"


def test_love_forty(game):
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    assert game.score() == "Love-Forty"


def test_love_all(game):
    assert game.score() == "Love-All"


def test_love_11(game):
    game.first_player_score()
    game.second_player_score()
    assert game.score() == "Fifteen-All"


def test_love_22(game):
    game.first_player_score()
    game.second_player_score()
    game.first_player_score()
    game.second_player_score()
    assert game.score() == "Thirty-All"


def test_love_33(game):
    game.first_player_score()
    game.second_player_score()
    game.first_player_score()
    game.second_player_score()
    game.first_player_score()
    game.second_player_score()
    assert game.score() == "Deuce"


def test_love_44(game):
    game.first_player_score()
    game.second_player_score()
    game.first_player_score()
    game.second_player_score()
    game.first_player_score()
    game.second_player_score()
    game.first_player_score()
    game.second_player_score()
    assert game.score() == "Deuce"


def test_43(game):
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    assert game.score() == "Mason Adv"


def test_53(game):
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    assert game.score() == "Mason Win"



def test_34(game):
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    assert game.score() == "Rina Adv"


def test_35(game):
    game.first_player_score()
    game.first_player_score()
    game.first_player_score()
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    game.second_player_score()
    assert game.score() == "Rina Win"

