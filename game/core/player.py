from game.core.symbol import Symbol
from game.exceptions.core_exceptions import SymbolError


class Player:
    __slots__ = "name", "symbol", "count_steps"

    def __new__(cls, name, symbol):
        if not isinstance(symbol, Symbol):
            raise SymbolError

        instance = super().__new__(cls)
        return instance

    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol
        self.count_steps = 0


