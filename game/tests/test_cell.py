import pytest
from game.core.table.cell import Cell
from game.core.symbol import Symbol
from game.exceptions.core_exceptions import SymbolError


def test_set_cell_value_error():
    with pytest.raises(SymbolError):
        Cell("0")

    with pytest.raises(SymbolError):
        Cell(3)

    with pytest.raises(SymbolError):
        Cell(Symbol)


def test_set_cell_true():
    cell = Cell(Symbol.O)
    assert cell.symbol in Symbol

    cell = Cell(Symbol.X)
    assert cell.symbol == Symbol.X
