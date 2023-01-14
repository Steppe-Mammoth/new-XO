from abc import ABC
from enum import Enum

from game.core.symbol import Symbol
from game.exceptions.core_exceptions import SymbolError


class PlayerBase(ABC):
    class Role(Enum):
        USER = 1
        ANDROID = 2

    __slots__ = "name", "_symbol", "_count_steps", "_role"

    def __init__(self, name: str, symbol: Symbol, role: Role):
        self.name = name
        self._symbol = symbol
        self._count_steps = 0
        self._role = role

    @property
    def symbol(self) -> Symbol:  # add test
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

    def __init__(self, name: str, symbol: Symbol, role: Role = Role.USER):
        if not isinstance(symbol, Symbol):
            raise SymbolError
        if role not in self.Role:
            raise AttributeError('Bad role')  # зробить виключення

        super().__init__(name=name, symbol=symbol, role=role)


p1 = Player(name='Igor1', symbol=Symbol('X', 1))
p2 = Player(name='Igor1', symbol=Symbol('X', 1), role=Player.Role.ANDROID)
