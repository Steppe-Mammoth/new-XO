# Do not use methods from this builder, it is for testing purposes only.

from typing import Type, Literal

from game import Player
from game.core.players.player import PlayerT, Role
from game.core.symbol import SymbolBase, Symbol
from game.core.table.param import TableParam
from game.core.table.table import TableDefault, TableBase


def build_table(row: int,
                column: int,
                comb: int,
                table_t: Type[TableBase] = TableDefault):
    param1 = TableParam(ROW=row, COLUMN=column, COMBINATION=comb)
    return table_t(param1)


def build_player(name: str,
                 symbol: SymbolBase,
                 player_t: Type[PlayerT],
                 role: Player.Role = Role.USER) -> PlayerT:
    player: PlayerT = player_t(name=name, role=role, symbol=symbol)
    return player


def build_player_list(player_t: Type[PlayerT] = Player,
                      symbol_t: Type[SymbolBase] = Symbol,
                      size: Literal[1, 2, 3] = 3) -> list[PlayerT]:
    players_list = []

    names = ('Vasya-1', 'Egor-2', 'Android Vera-3')
    roles = (Role.USER, Role.USER, Role.ANDROID)
    symbol_name = ['X', 'O', 'I']

    for i in range(size):
        players_list.append(player_t(name=names[i], symbol=symbol_t(symbol_name[i]), role=roles[i]))

    return players_list
