from typing import Any, Tuple, List, Sequence
from abc import ABC, abstractmethod

from game.core.table.combinations import CombDefault, CombinationsBase, check_combinations_instance
from game.core.table.annotations import CombsType
from game.core.table.cell import Cell

from game.core.symbol import SymbolBase
from game.core.table.param import TableParam, check_table_param_instance
from game.exceptions.core_exceptions import CellAlreadyUsedError, TableIndexError, TableInstanceError, AllCellsUsedError


def create_2d_list(row: int, column: int, default_obj: Any = None) -> Tuple[List[Any | None]]:
    return tuple([default_obj for _ in range(row)] for _ in range(column))  # add instance checker


class TableBase(ABC):
    __slots__ = "_param", "_table", "_combinations", "_count_free_cells"

    def __init__(self, param: TableParam, combinations: CombinationsBase):

        check_table_param_instance(param)
        check_combinations_instance(combinations)

        self._param = param
        self._count_free_cells: int = param.ROW * param.COLUMN
        self._table = self.get_new_playing_field(param=param)
        self._combinations = combinations.get_combinations(size_row=param.ROW,
                                                           size_column=param.COLUMN,
                                                           size_combination=param.COMBINATION)

    @property
    def param(self) -> TableParam:
        return self._param

    @property  # Reassign for those who care about security, because modifiable objects are returned.
    def table(self) -> Sequence[List[Cell | None]]:
        return self._table

    @property  # Reassign for those who care about security, because modifiable objects are returned.
    def combinations(self) -> CombsType:
        return self._combinations

    @property
    def count_free_cells(self):
        return self._count_free_cells

    def _remove_free_cell(self):
        self._count_free_cells -= 1

    @abstractmethod
    def set_symbol_cell(self, index_row: int, index_column: int, symbol: SymbolBase):
        """
        Sets the transferred character in the specified cell by the row and column indices of the table \n
        * Subtracts the number of free cells by -1 after successful installation.
        """
        ...
        self._remove_free_cell()

    @classmethod
    @abstractmethod
    def get_new_playing_field(cls, param: TableParam) -> Tuple[List[None]]:
        pass


class TableDefault(TableBase):

    def __init__(self, param: TableParam, combinations: CombinationsBase = CombDefault()):
        super().__init__(param, combinations=combinations)

    def set_symbol_cell(self, index_row: int, index_column: int, symbol: SymbolBase):
        if self.count_free_cells == 0:
            raise AllCellsUsedError(game_table=self.table)

        param = self._param
        table = self._table

        if not (param.ROW - 1 >= index_row >= 0) or not (param.COLUMN - 1 >= index_column >= 0):
            raise TableIndexError(index_column, index_row=index_row, table_param=param)

        if table[index_row][index_column] is not None:
            used_cell: Cell = table[index_row][index_column]
            raise CellAlreadyUsedError(used_cell.symbol.name, new_symbol=symbol.name)

        table[index_row][index_column] = Cell(symbol=symbol)
        self._remove_free_cell()

    def get_new_playing_field(self, param: TableParam) -> Tuple[List[None]]:
        return create_2d_list(row=param.ROW, column=param.COLUMN, default_obj=None)


def check_table_instance(table: TableBase):
    if not isinstance(table, TableBase):
        raise TableInstanceError
