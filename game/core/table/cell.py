from abc import ABC

from game.core.symbol import Symbol, check_symbol


class CellBase(ABC):
    __slots__ = "_symbol",

    def __init__(self, symbol: Symbol):
        check_symbol(symbol)
        self._symbol = symbol

    @property
    def symbol(self) -> Symbol:
        return self._symbol


class Cell(CellBase):
    pass
