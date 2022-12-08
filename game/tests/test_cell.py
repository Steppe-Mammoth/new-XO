import pytest
from game.core.cell import Cell, CellName


def test_set_cell_value_error():
    cell = Cell()
    with pytest.raises(ValueError):
        cell.symbol = "0"


def test_set_cell_true():
    cell = Cell()
    cell.symbol = CellName.CELL_O
    assert (cell.symbol in CellName)


def test_reset_symbol_cell():
    c = Cell()
    c.symbol = CellName.CELL_O

    with pytest.raises(IOError):
        c.symbol = CellName.CELL_X
