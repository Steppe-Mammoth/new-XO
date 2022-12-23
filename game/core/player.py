from game.core.symbol import Symbol
from game.exceptions.core_exceptions import SymbolError


class Player:
    __slots__ = "name", "symbol", "_count_steps"

    def __new__(cls, name, symbol):
        if not isinstance(symbol, Symbol):
            raise SymbolError

        instance = super().__new__(cls)
        return instance

    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol
        self._count_steps = 0

    @property
    def count_steps(self):
        return self._count_steps

    def add_step(self):
        self._count_steps += 1
