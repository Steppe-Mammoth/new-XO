import copy
from enum import Enum
from cell import Cell, Symbol


class TableSize(Enum):
    DEFAULT = 9


class Table:
    def __init__(self, size: TableSize):
        self._table: list[Cell] = []
        self.size: TableSize = size

        self._create_table(size)

    def _create_table(self, size):
        if not isinstance(size, TableSize):
            raise ValueError('You args not support. Send only TableSize arg')

        for i in range(size.value):
            self._table.append(Cell())

    def get_table(self):
        return copy.deepcopy(self._table)

    def set_symbol_cell(self, index: int, symbol: Symbol):
        size: int = self.size.value

        if index > size:
            raise IndexError(f'Index cell > size this table. {index} > {self.size.value}')

        self._table[index].symbol = symbol
