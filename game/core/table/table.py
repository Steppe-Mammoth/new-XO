from typing import Any, Union

from game.core.table.combinations import Combinations
from game.core.table.cell import Cell

from game.core.symbol import Symbol
from game.core.table.param import TableParam, AllowedTableParameter
from game.exceptions.core_exceptions import CellAlreadyUsedError, TableIndexError, TableParametersError


class TableMeta:
    ONLY_ALLOWED_TABLE_PARAMETERS = False

    def __new__(cls, param):
        if cls.ONLY_ALLOWED_TABLE_PARAMETERS:
            if not isinstance(param, AllowedTableParameter):
                raise TableParametersError
        else:
            if not isinstance(param, TableParam) and not isinstance(param, AllowedTableParameter):
                raise TableParametersError

        instance = super().__new__(cls)
        return instance


class Table(TableMeta):
    __slots__ = "_param", "_table", "_combinations"

    def __init__(self, param: Union[AllowedTableParameter, TableParam]):
        if isinstance(param, AllowedTableParameter):
            param = param.value

        self._param: TableParam = param
        self._table = create_2d_list(column=self._param.COLUMN,
                                     row=self._param.ROW,
                                     default_obj=None)

        self._combinations = Combinations.get_combinations(size_row=self._param.ROW,
                                                           size_column=self._param.COLUMN,
                                                           size_combination=self._param.COMBINATION)

    @property
    def param(self):
        return self._param

    @property
    def table(self):
        return self._table

    @property
    def combinations(self):
        return self._combinations

    def set_symbol_cell(self, index_row: int, index_column: int, symbol: Symbol):
        param = self._param
        table = self._table

        if not (param.ROW - 1 >= index_row >= 0) or not (param.COLUMN - 1 >= index_column >= 0):
            raise TableIndexError(index_column, index_row=index_row, table_param=param)

        if table[index_row][index_column] is not None:
            used_cell: Cell = table[index_row][index_column]
            raise CellAlreadyUsedError(used_cell.symbol, new_cell=symbol)

        table[index_row][index_column] = Cell(symbol=symbol)


def create_2d_list(column: int, row: int, default_obj: any) -> tuple[list[Any]]:
    return tuple([default_obj for x in range(row)] for y in range(column))
