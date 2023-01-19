from abc import ABC

from game.core.symbol import SymbolBase, check_symbol


class CellBase(ABC):
    __slots__ = "_symbol",

    def __init__(self, symbol: SymbolBase):
        check_symbol(symbol)
        self._symbol = symbol

    @property
    def symbol(self) -> SymbolBase:
        return self._symbol


class Cell(CellBase):
    pass
