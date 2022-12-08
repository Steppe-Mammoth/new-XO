import pytest
from game.core.cell import Cell, Symbol


def test_set_cell_value_error():
    cell = Cell()
    with pytest.raises(ValueError):
        cell.symbol = "0"


def test_set_cell_true():
    cell = Cell()
    cell.symbol = Symbol.O
    assert (cell.symbol in Symbol)


def test_reset_symbol_cell():
    c = Cell()
    c.symbol = Symbol.O

    with pytest.raises(IOError):
        c.symbol = Symbol.X
