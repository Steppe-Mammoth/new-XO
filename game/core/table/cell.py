from abc import ABC

from game.core.symbol import Symbol
from game.exceptions.core_exceptions import SymbolError


class CellBase(ABC):
    __slots__ = "_symbol",

    def __init__(self, symbol):
        self._symbol = symbol

    @property
    def symbol(self):
        return self._symbol


class Cell(CellBase):
    def __init__(self, symbol: Symbol):
        if not isinstance(symbol, Symbol):
            raise SymbolError

        super().__init__(symbol)
