import copy
from typing import Any, Union

from game.core.table.cell import Cell

from game.core.symbol import Symbol
from game.core.table.param import TableParam, AllowedTableParameter
from game.exceptions.core_exceptions import CellAlreadyUsedError, TableIndexError, TableParametersError


ONLY_ALLOWED_TABLE_PARAMETERS = True


class TableMeta:

    def __new__(cls, param):
        if ONLY_ALLOWED_TABLE_PARAMETERS:
            if not isinstance(param, AllowedTableParameter):
                raise TableParametersError
        else:
            if not isinstance(param, TableParam) and not isinstance(param, AllowedTableParameter):
                raise TableParametersError

        instance = super().__new__(cls)
        return instance


class Table(TableMeta):
    def __init__(self, param: Union[AllowedTableParameter, TableParam]):
        if isinstance(param, AllowedTableParameter):
            param = param.value

        self.__param: TableParam = param
        self.__table = create_2d_list(column=self.__param.COLUMN, row=self.__param.ROW, default_obj=None)

    @property
    def param(self):
        return self.__param

    @property
    def table(self):
        return copy.deepcopy(self.__table)

    def set_symbol_cell(self, index_column: int, index_row: int, symbol: Symbol):
        param = self.__param
        table = self.__table

        if not (param.COLUMN-1 >= index_column >= 0) or not (param.ROW-1 >= index_row >= 0):
            raise TableIndexError(index_column, index_row=index_row, table_param=param)

        if table[index_column][index_row] is not None:
            used_cell: Cell = table[index_column][index_row]
            raise CellAlreadyUsedError(used_cell.symbol, new_cell=symbol)

        table[index_column][index_row] = Cell(symbol=symbol)


def create_2d_list(column: int, row: int, default_obj: any) -> tuple[list[Any]]:
    return tuple([default_obj for x in range(row)] for y in range(column))
