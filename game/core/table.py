import copy
from enum import Enum, verify, UNIQUE
from dataclasses import dataclass
from typing import Tuple, List, Any

from game.core.cell import Cell
from game.core.symbol import Symbol


@dataclass(frozen=True)
class TableParam:
    ROW: int
    COLUMN: int
    COMBINATION: int


@verify(UNIQUE)
class AllowedTableParameter(Enum):
    DEFAULT = TableParam(ROW=3, COLUMN=3, COMBINATION=3)


def create_2d_list(column: int, row: int, default_object: any) -> tuple[list[Any]]:
    return tuple([default_object for x in range(row)] for y in range(column))


class TableMeta:
    def __new__(cls, param):
        if param not in [param for param in AllowedTableParameter]:
            raise ValueError('This parameters(TableParams) is not supported.'
                             'Send only parameters set in "AllowedTableParameter\n'
                             'Example: Table(AllowedTableParameter.DEFAULT)"')

        instance = super().__new__(cls)
        return instance


class Table(TableMeta):
    def __init__(self, param: AllowedTableParameter):
        self.__param: TableParam = param.value
        self.__table: tuple[list] = create_2d_list(column=self.__param.COLUMN,
                                                   row=self.__param.ROW,
                                                   default_object=None)

    @property
    def param(self):
        return self.__param

    @property
    def table(self):
        return copy.deepcopy(self.__table)

    def set_symbol_cell(self, index_column: int, index_row, symbol: Symbol):
        param = self.__param
        table = self.__table

        if not index_column < param.COLUMN > 0:
            raise IndexError(f'You send {index_column} index for column.\n'
                             f'Possible index is set in the column: MAX = {param.COLUMN - 1}, MIN = 0')

        if not index_row < param.ROW > 0:
            raise IndexError(f'You send {index_row} index for row.\n'
                             f'Possible index is set in the row: MAX = {param.ROW - 1}, MIN = 0')

        if table[index_column][index_row] is not None:
            used_cell: Cell = table[index_column][index_row]
            raise IOError(f'This cell is used. Cell symbol now = {used_cell.symbol.name}, you send = {symbol.name}')

        table[index_column][index_row] = Cell(symbol=symbol)
