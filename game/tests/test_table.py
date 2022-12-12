import pytest
from game.core.symbol import Symbol
from game.core.table.param import AllowedTableParameter, TableParam
from game.core.table.table import Table
from game.exceptions.core_exceptions import CellAlreadyUsedError, TableIndexError, TableParametersError


def build_table() -> Table:
    return Table(param=AllowedTableParameter.DEFAULT)


def test_table_init_default_true():
    default_table = tuple([None for x in range(3)] for y in range(3))

    table1 = Table(param=AllowedTableParameter.DEFAULT).table
    assert default_table == table1


def test_table_init_user_true():
    default_table = tuple([None for x in range(10)] for y in range(8))
    Table.ONLY_ALLOWED_TABLE_PARAMETERS = False

    table1 = Table(param=TableParam(10, 8, 8)).table
    assert default_table == table1

    Table.ONLY_ALLOWED_TABLE_PARAMETERS = True


def test_table_init_error():
    with pytest.raises(TableParametersError):
        param = TableParam(ROW=5, COLUMN=10, COMBINATION=3)
        t = Table(param=param)

    with pytest.raises(TableParametersError):
        param = TableParam(ROW=3, COLUMN=3, COMBINATION=3)
        t = Table(param=param)

    with pytest.raises(TableParametersError):
        param = "2323232"
        t = Table(param=param)



def test_set_symbol_cell_true():
    table = build_table()

    table.set_symbol_cell(index_column=2, index_row=2, symbol=Symbol.O)
    assert table.table[2][2].symbol == Symbol.O

    table.set_symbol_cell(index_column=1, index_row=1, symbol=Symbol.X)
    assert table.table[1][1].symbol == Symbol.X

    table.set_symbol_cell(index_column=0, index_row=1, symbol=Symbol.X)
    assert table.table[0][1].symbol == Symbol.X


def test_set_symbol_cell_index_error():
    table = build_table()

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=1, index_row=3, symbol=Symbol.X)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=3, index_row=1, symbol=Symbol.O)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=3, index_row=3, symbol=Symbol.O)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=-1, index_row=2, symbol=Symbol.O)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=2, index_row=-1, symbol=Symbol.O)


def test_reset_symbol_cell():
    table = build_table()

    table.set_symbol_cell(index_column=2, index_row=1, symbol=Symbol.O)
    table.set_symbol_cell(index_column=1, index_row=2, symbol=Symbol.O)
    table.set_symbol_cell(index_column=0, index_row=1, symbol=Symbol.O)

    with pytest.raises(CellAlreadyUsedError):
        table.set_symbol_cell(index_column=2, index_row=1, symbol=Symbol.X)

    with pytest.raises(CellAlreadyUsedError):
        table.set_symbol_cell(index_column=1, index_row=2, symbol=Symbol.O)

    with pytest.raises(CellAlreadyUsedError):
        table.set_symbol_cell(index_column=0, index_row=1, symbol=Symbol.X)