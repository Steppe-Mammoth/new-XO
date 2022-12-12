import random
from typing import Any, NamedTuple

from game.core.symbol import Symbol
from game.core.table.table import Table, AllowedTableParameter


class Steps(NamedTuple):
    free_cells: list[tuple[int, int]]
    my_steps: list[tuple[int, int]]
    enemy_steps: list[tuple[int, int]]


table = Table(AllowedTableParameter.DEFAULT)
table.set_symbol_cell(index_row=1, index_column=2, symbol=Symbol.X)


class FindCellAI:

    @classmethod
    def find_all_steps_in_tablr(cls, table: tuple[list[Any]], my_symbol: Symbol, size_combination: int):
        free_cells = []
        my_steps = []
        enemy_steps = []

        for index_row, row in enumerate(table):
            for index_cell, cell in enumerate(row):
                if cell is None:
                    free_cells.append((index_row, index_cell))
                elif cell.symbol == my_symbol:
                    my_steps.append((index_row, index_cell))
                else:
                    enemy_steps.append((index_row, index_cell))

        return Steps(free_cells=free_cells, my_steps=my_steps, enemy_steps=enemy_steps)

    @classmethod
    def find_best_step(cls, steps: Steps, size_combinations: int):
        my_best_steps = []
        enemy_best_steps = []

        if len(steps.my_steps) == 0:
            return random.choice(steps.free_cells)

        for step in steps.my_steps:
            pass




a = FindCellAI.find_all_steps_in_tablr(table.table, my_symbol=Symbol.X, size_combination=table.param.COMBINATION)