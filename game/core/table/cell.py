from game.core.symbol import Symbol
from game.exceptions.core_exceptions import SymbolError


class CellMeta:
    def __new__(cls, symbol):
        if not isinstance(symbol, Symbol):
            raise SymbolError
        return super().__new__(cls)

    def __deepcopy__(self, memo):
        return self


class Cell(CellMeta):
    __slots__ = "__symbol",

    def __init__(self, symbol: Symbol):
        self.__symbol = symbol

    @property
    def symbol(self) -> Symbol:
        return self.__symbol
