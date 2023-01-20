from abc import ABC
from enum import Enum
from typing import Literal, TypeVar

from game.core.symbol import SymbolBase, verify_symbol
from game.exceptions.core_exceptions import BadRoleError, PlayerInstanceError

PlayerT = TypeVar('PlayerT', bound='PlayerBase')


class PlayerBase(ABC):
    class Role(Enum):
        USER = 1
        ANDROID = 2

    __slots__ = "name", "_symbol", "_count_steps", "_role"

    def __init__(self, name: str, symbol: SymbolBase, role: Literal[Role.USER, Role.ANDROID]):
        verify_role(role=role)
        verify_symbol(symbol)

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

    def __init__(self, name: str, symbol: SymbolBase, role=Role.USER):
        super().__init__(name=name, symbol=symbol, role=role)


def verify_role(role: PlayerBase.Role):
    if not type(role) is PlayerBase.Role or role not in PlayerBase.Role:
        raise BadRoleError


def verify_player_instance(player: PlayerBase):
    if not isinstance(player, PlayerBase):
        raise PlayerInstanceError
