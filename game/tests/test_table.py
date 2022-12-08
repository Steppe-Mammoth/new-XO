import pytest
from game.core.cell import CellName, Cell
from game.core.table import Table, TableSize


def test_init_table_true():
    default_size_cells_list: list[Cell] = [Cell() for i in range(TableSize.DEFAULT.value)]
    table = Table(size=TableSize.DEFAULT)
    assert (table.get_table(), default_size_cells_list)


def test_init_table_value_error():
    with pytest.raises(ValueError):
        t = Table(size=8)


def test_set_symbol_cell_true():
    table = Table(size=TableSize.DEFAULT)
    table.set_symbol_cell(5, symbol=CellName.CELL_X)
    assert (table.get_table()[5].symbol, CellName.CELL_X)


def test_set_symbol_cell_index_error():
    table = Table(size=TableSize.DEFAULT)
    with pytest.raises(IndexError):
        table.set_symbol_cell(10, symbol=CellName.CELL_O)


def test_reset_symbol_cell():
    table = Table(size=TableSize.DEFAULT)
    table.set_symbol_cell(5, symbol=CellName.CELL_X)

    with pytest.raises(IOError):
        table.set_symbol_cell(5, symbol=CellName.CELL_X)
