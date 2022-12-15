from game.core.AI import FindCellAI
from game.core.symbol import Symbol
from game.core.table.param import AllowedTableParameter
from game.core.table.table import Table


def build_table():
    return Table(param=AllowedTableParameter.DEFAULT)


def test_ai_3_3_3_3_fist_step():
    t = build_table()
    ai_all_step = FindCellAI.find_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)
    ai_get_step = FindCellAI.get_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)
    assert ai_all_step == [list(comb) for comb in t.combinations]
    assert len(ai_all_step) == 8
    assert len(ai_get_step) == 2


def test_ai_3_3_3_1_my_win():
    t = build_table()

    t.set_symbol_cell(index_row=1, index_column=2, symbol=Symbol.X)  #
    t.set_symbol_cell(index_row=2, index_column=1, symbol=Symbol.O)
    t.set_symbol_cell(index_row=1, index_column=0, symbol=Symbol.X)  #
    t.set_symbol_cell(index_row=2, index_column=0, symbol=Symbol.O)

    ai_all_step = FindCellAI.find_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)
    ai_get_step = FindCellAI.get_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)
    assert ai_all_step == (1, 1)
    assert ai_get_step == (1, 1)


def test_ai_3_3_3_2_my_second_step():
    t = build_table()
    t.set_symbol_cell(index_row=2, index_column=0, symbol=Symbol.O)
    t.set_symbol_cell(index_row=1, index_column=0, symbol=Symbol.X)  #

    ai_all_step = FindCellAI.find_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)
    ai_get_step = FindCellAI.get_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)

    assert len(ai_all_step) == 1
    assert ai_all_step == [[(1, 1), (1, 2)]]
    assert ai_get_step == (1, 1) or ai_get_step == (1, 2)


def test_ai_3_3_3_1_fail_to_win_enemy():
    t = build_table()
    t.set_symbol_cell(index_row=0, index_column=2, symbol=Symbol.X)  #
    t.set_symbol_cell(index_row=2, index_column=0, symbol=Symbol.O)
    t.set_symbol_cell(index_row=1, index_column=0, symbol=Symbol.X)  #
    t.set_symbol_cell(index_row=2, index_column=1, symbol=Symbol.O)

    ai_all_step = FindCellAI.find_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)
    ai_get_step = FindCellAI.get_best_step(symbol=Symbol.X, table=t.table, combinations=t.combinations)
    assert ai_all_step == (2, 2)
    assert ai_get_step == (2, 2)