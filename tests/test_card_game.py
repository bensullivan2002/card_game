from src.card_game_main import Game


def test_new_game_starts_as_not_playing():
    new_game = Game()
    assert new_game.playing is False
