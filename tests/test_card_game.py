import pytest
from src.card_game_main import Game


def test_create_game():
    assert Game.create_game() == Game()
