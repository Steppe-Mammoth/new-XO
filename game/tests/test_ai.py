from typing import Tuple

from game.core.AI import AIFindDefault, AIFindBase
from game.core.cheker import CheckerDefault, CheckerBase
from game.core.players.player import Player
from game.core.symbol import Symbol
from game.core.table.param import TableParam
from game.core.table.table import TableDefault

p_ai = Player(name='AI', symbol=Symbol(name='X', value=1))
p_2 = Player(name='Petro', symbol=Symbol(name='O', value=2))

AI_FINDER: AIFindBase.__class__ = AIFindDefault
CHECKER: CheckerBase.__class__ = CheckerDefault


def build_table():
    param1 = TableParam(3, 3, 3)
    return TableDefault(param1)


def test_ai_all_result_for_first_step():
    t = build_table()
    ai_all_step = AI_FINDER._find_best_step(symbol=p_ai.symbol, table=t.table, combinations=t.combinations)
    ai_get_step = AI_FINDER.get_best_step(symbol=p_ai.symbol, table=t.table, combinations=t.combinations)
    assert ai_all_step == [list(comb) for comb in t.combinations]

    assert len(ai_all_step) == 8
    assert len(ai_get_step) == 2


def test_ai_one_player_win_3():
    t = build_table()
    for i in range(3):
        i_row, i_column = AI_FINDER.get_best_step(combinations=t.combinations, symbol=p_ai.symbol, table=t.table)
        t.set_symbol_cell(index_row=i_row, index_column=i_column, symbol=p_ai.symbol)

    result = CHECKER.result_player(symbol=p_ai.symbol, table=t.table, combinations=t.combinations)
    print(result)

    assert isinstance(result, Tuple) and result in t.combinations


def test_ai_all_result_second_step():
    t = build_table()
    t.set_symbol_cell(index_row=2, index_column=0, symbol=p_2.symbol)
    t.set_symbol_cell(index_row=1, index_column=0, symbol=p_ai.symbol)  #

    ai_all_step = AI_FINDER._find_best_step(symbol=p_ai.symbol, table=t.table, combinations=t.combinations)
    ai_get_step = AI_FINDER.get_best_step(symbol=p_ai.symbol, table=t.table, combinations=t.combinations)

    assert ai_all_step == [[(1, 1), (1, 2)]]
    assert ai_get_step in ((1, 1), (1, 2))


def test_ai_battle_1_fail_to_win_enemy_3():  # Перебити гравця не давши зібрати 3/3
    t = build_table()
    # comb for player ((1, 2), (1, 0), (*1, 1*))
    t.set_symbol_cell(index_row=1, index_column=2, symbol=p_2.symbol)
    t.set_symbol_cell(index_row=0, index_column=0, symbol=p_ai.symbol)  #
    t.set_symbol_cell(index_row=1, index_column=0, symbol=p_2.symbol)

    i_row, i_column = AI_FINDER.get_best_step(symbol=p_ai.symbol, table=t.table, combinations=t.combinations)
    t.set_symbol_cell(index_row=i_row, index_column=i_column, symbol=p_ai.symbol)  #

    assert t.table[1][1].symbol == p_ai.symbol


def test_ai_battle_2_fail_to_win_enemy_3():
    t = build_table()
    t.set_symbol_cell(index_row=0, index_column=2, symbol=p_ai.symbol)  #
    t.set_symbol_cell(index_row=2, index_column=0, symbol=p_2.symbol)
    t.set_symbol_cell(index_row=1, index_column=0, symbol=p_ai.symbol)  #
    t.set_symbol_cell(index_row=2, index_column=1, symbol=p_2.symbol)

    ai_get_step = AI_FINDER.get_best_step(symbol=p_ai.symbol, table=t.table, combinations=t.combinations)
    assert ai_get_step == (2, 2)
