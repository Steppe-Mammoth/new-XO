from typing import Any, Tuple, List, Sequence
from abc import ABC, abstractmethod

from game.core.table.combinations import CombDefault, CombinationsBase
from game.core.table.annotations import CombsType
from game.core.table.cell import Cell

from game.core.symbol import Symbol
from game.core.table.param import TableParam
from game.exceptions.core_exceptions import CellAlreadyUsedError, TableIndexError, TableParametersError


def create_2d_list(row: int, column: int, default_obj: Any = None) -> Tuple[List[Any | None]]:
    return tuple([default_obj for _ in range(row)] for _ in range(column))


class TableBase(ABC):
    __slots__ = "_param", "_table", "_combinations", "_count_free_cells"

    def __init__(self, param: TableParam, combinations: CombinationsBase):

        if not isinstance(param, TableParam):
            raise TableParametersError
        if not isinstance(combinations, CombinationsBase):
            raise ValueError('Need class CombinationsBase')  # make exception

        self._table: Sequence[List[None | Cell]]
        self._create_table(param=param)

        self._param = param
        self._count_free_cells: int = param.ROW * param.COLUMN
        self._combinations = combinations.get_combinations(size_row=param.ROW,
                                                           size_column=param.COLUMN,
                                                           size_combination=param.COMBINATION)

    @abstractmethod
    def set_symbol_cell(self, index_row: int, index_column: int, symbol: Symbol):
        if self.count_free_cells > 0:
            ...
        self._remove_free_cell()

    @property
    def param(self) -> TableParam:
        return self._param

    @property  # Перезначати, тим хто піклується про безпеку, бо повертаються змінюванні об'єкти
    def table(self) -> Sequence[List[Cell | None]]:
        return self._table

    @property  # Перезначати, тим хто піклується про безпеку, бо повертаються змінюванні об'єкти
    def combinations(self) -> CombsType:
        return self._combinations

    @property
    def count_free_cells(self):
        return self._count_free_cells

    def _remove_free_cell(self):
        self._count_free_cells -= 1

    def _create_table(self, param: TableParam):
        self._table = create_2d_list(row=param.ROW, column=param.COLUMN, default_obj=None)


class TableDefault(TableBase):

    def __init__(self, param: TableParam, combinations: CombinationsBase = CombDefault()):
        super().__init__(param, combinations=combinations)

    def set_symbol_cell(self, index_row: int, index_column: int, symbol: Symbol):
        if self.count_free_cells == 0:
            raise AttributeError('ALL USED CELLS')

        param = self._param
        table = self._table

        if not (param.ROW - 1 >= index_row >= 0) or not (param.COLUMN - 1 >= index_column >= 0):
            raise TableIndexError(index_column, index_row=index_row, table_param=param)

        if table[index_row][index_column] is not None:
            used_cell: Cell = table[index_row][index_column]
            raise CellAlreadyUsedError(used_cell.symbol, new_cell=symbol)

        table[index_row][index_column] = Cell(symbol=symbol)
        self._remove_free_cell()
