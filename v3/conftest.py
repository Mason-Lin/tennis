from .tennis import TennisGame

import pytest


@pytest.fixture()
def game():
    return TennisGame("Mason", "Rina")
