from .tennis import TennisGame

def test_Love_All():
    game = TennisGame()
    score = game.Score()
    assert score == "Love All"
