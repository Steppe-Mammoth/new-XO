from enum import Enum
from typing import Optional


class Symbol(Enum):
    X = 1
    O = 0


class Cell:
    def __init__(self):
        self._symbol: Optional[Symbol] = None

    @property
    def symbol(self) -> Symbol:
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: Symbol):
        if not isinstance(symbol, Symbol):
            raise ValueError('Need only CellName')

        if self.symbol is not None:
            raise IOError(f'This cell is used. Cell symbol now {self.symbol.name}, you send {symbol.name}', )

        self._symbol = symbol
