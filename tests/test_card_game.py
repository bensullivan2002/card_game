from src.card_game_main import Game
import pytest


def test_new_game_starts_as_not_playing():
    new_game = Game()
    assert new_game.playing is False


@pytest.mark.parametrize(
    "player, expected",
    [
        pytest.param("Ben", ["Ben"]),
        pytest.param("", [""])
    ],
)
def test_add_player(player, expected):
    game = Game()
    game.add_player(player)
    assert game.players == expected
