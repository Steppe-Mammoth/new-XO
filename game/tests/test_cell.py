import pytest
from game.core.cell import Cell
from game.core.symbol import Symbol


def test_set_cell_value_error():
    with pytest.raises(ValueError):
        Cell("0")

    with pytest.raises(ValueError):
        Cell(3)

    with pytest.raises(ValueError):
        Cell(Symbol)


def test_set_cell_true():
    cell = Cell(Symbol.O)
    assert cell.symbol in Symbol

    cell = Cell(Symbol.X)
    assert cell.symbol == Symbol.X
