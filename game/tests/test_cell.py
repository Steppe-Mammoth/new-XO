import pytest
from game.core.table.cell import Cell
from game.exceptions.core_exceptions import SymbolError
from game.core.symbol import Symbol


def test_init_cell_true():
    for symbol_name in ['X', 'QWQ', 1, 2, [234]]:
        symbol = Symbol(name=symbol_name)
        cell = Cell(symbol=symbol)


def test_init_cell_error():
    for bad_symbol in ['X', 'QWQ', 1, 2, [234]]:
        with pytest.raises(SymbolError):
            cell = Cell(symbol=bad_symbol)
