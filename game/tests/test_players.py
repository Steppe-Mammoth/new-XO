from typing import Type, Literal
import pytest

from game.core.players.player import PlayerBase, Player
from game.core.players.players import PlayersBase, Players
from game.core.symbol import SymbolBase, Symbol
from game.exceptions.core_exceptions import PlayerInstanceError, PlayersIsEmptyError
from game.tests.builder import build_player_list

PLAYERS: Type[PlayersBase] = Players
PLAYER: Type[PlayerBase] = Player
SYMBOL: Type[SymbolBase] = Symbol


def fast_build_player_list(size: Literal[1, 2, 3] = 3):
    return build_player_list(player_t=PLAYER, symbol_t=SYMBOL, size=size)


def test_init_players():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)

    assert ps.player_list == player_list
    assert ps.current_player == player_list[0]


def test_bad_verify_players_list():
    player_list = fast_build_player_list()
    player_list.append('Sergo_2008')

    with pytest.raises(PlayerInstanceError):
        PLAYERS(players=player_list)

    with pytest.raises(PlayersIsEmptyError):
        PLAYERS(players=[])


def test_set_next_player1():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[0]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[1]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[2]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[0]


def test_set_next_player2():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)

    assert ps.current_player == player_list[0]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[1]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[2]


def test_shuffle_players():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)
    assert ps.player_list == player_list

    ps.shuffle_players()
    assert player_list != ps.player_list

    assert ps.current_player == ps.player_list[0]
