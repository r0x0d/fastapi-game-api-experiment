from carnage.players.player import Player


def test_player_can_initialize():
    player = Player()
    assert isinstance(player, Player)
