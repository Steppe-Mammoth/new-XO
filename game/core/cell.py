from enum import Enum
from typing import Optional


class CellName(Enum):
    CELL_X = 1
    CELL_O = 0


class Cell:
    def __init__(self):
        self._symbol: Optional[CellName] = None

    @property
    def symbol(self) -> CellName:
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: CellName):
        if not isinstance(symbol, CellName):
            raise ValueError('Need only CellName')

        if self.symbol is not None:
            raise IOError(f'This cell is used. Cell symbol now {self.symbol.name}, you send {symbol.name}', )

        self._symbol = symbol