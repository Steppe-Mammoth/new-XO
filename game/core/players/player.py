from abc import ABC
from enum import Enum
from typing import Sequence

from game.core.symbol import SymbolBase, check_symbol
from game.exceptions.core_exceptions import PlayersIsEmptyError, BadRoleError, PlayerInstanceError


class PlayerBase(ABC):
    class Role(Enum):
        USER = 1
        ANDROID = 2

    __slots__ = "name", "_symbol", "_count_steps", "_role"

    def __init__(self, name: str, symbol: SymbolBase, role: Role):
        CheckPlayers.role(role=role)
        check_symbol(symbol)

        self.name = name
        self._symbol = symbol
        self._count_steps = 0
        self._role = role

    @property
    def symbol(self) -> SymbolBase:  # add test
        return self._symbol

    @property
    def count_steps(self) -> int:  # add test
        return self._count_steps

    @property
    def role(self) -> Role:
        return self._role

    def add_count_step(self):
        self._count_steps += 1  # add test


class Player(PlayerBase):
    Role = PlayerBase.Role

    def __init__(self, name: str, symbol: SymbolBase, role: Role = Role.USER):
        super().__init__(name=name, symbol=symbol, role=role)


class CheckPlayers:
    @classmethod
    def role(cls, role: PlayerBase.Role):
        if not type(role) is PlayerBase.Role or role not in PlayerBase.Role:
            raise BadRoleError

    @classmethod
    def player_instance(cls, player: PlayerBase):
        if not isinstance(player, PlayerBase):
            raise PlayerInstanceError

    @classmethod
    def list_players(cls, players: Sequence[PlayerBase]):
        if len(players) == 0:
            raise PlayersIsEmptyError
        for p in players:
            cls.player_instance(p)
