from game.core.symbol import Symbol
from game.core.table import Table, AllowedTableParameter
from game.core.cheker import CheckerTable

def build_table():
    return Table(param=AllowedTableParameter.DEFAULT)


def set_steps_return_tables():
    t1 = build_table()
    t1.set_symbol_cell(0, 0, symbol=Symbol.O) #
    t1.set_symbol_cell(1, 1, symbol=Symbol.O)
    t1.set_symbol_cell(1, 0, symbol=Symbol.X)
    t1.set_symbol_cell(2, 1, symbol=Symbol.X)
    t1.set_symbol_cell(0, 1, symbol=Symbol.O) #
    t1.set_symbol_cell(2, 2, symbol=Symbol.X)
    t1.set_symbol_cell(0, 2, symbol=Symbol.O) #

    t2 = build_table()
    t2.set_symbol_cell(0, 1, symbol=Symbol.O) #
    t2.set_symbol_cell(1, 1, symbol=Symbol.O) #
    t2.set_symbol_cell(2, 0, symbol=Symbol.X)
    t2.set_symbol_cell(0, 0, symbol=Symbol.X)
    t2.set_symbol_cell(2, 2, symbol=Symbol.X)
    t2.set_symbol_cell(0, 2, symbol=Symbol.X)
    t2.set_symbol_cell(2, 1, symbol=Symbol.O) #

    return t1, t2

def test_result():
    t1, t2 = set_steps_return_tables()
    result_O_table1 = CheckerTable.check_table_for_player(symbol=Symbol.O, table=t1.table, size_combination=t1.param.COMBINATION)
    result_X_table1 = CheckerTable.check_table_for_player(symbol=Symbol.X, table=t1.table, size_combination=t1.param.COMBINATION)

    result_O_table2 = CheckerTable.check_table_for_player(symbol=Symbol.O, table=t2.table, size_combination=t2.param.COMBINATION)
    result_X_table2 = CheckerTable.check_table_for_player(symbol=Symbol.X, table=t2.table, size_combination=t2.param.COMBINATION)

    assert result_O_table1 == [(0, 0), (0, 1), (0, 2)]
    assert result_X_table1 is None

    assert result_O_table2 == [(0, 1), (1, 1), (2, 1)]
    assert result_X_table2 is None
