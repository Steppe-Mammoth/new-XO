import random
from abc import ABC, abstractmethod
from typing import List, Sequence, Union

from game.core.symbol import Symbol
from game.core.table.annotations import CellIndex, CombsType
from game.core.table.cell import Cell


ListCombsType = List[List[CellIndex]]


class AIFindBase(ABC):
    @abstractmethod
    def get_best_step(self,
                      symbol: Symbol,
                      table: Sequence[List[Cell | None]],
                      combinations: CombsType) -> CellIndex:
        pass


class AIFindDefault(AIFindBase):
    @classmethod
    def get_best_step(cls,
                      symbol: Symbol,
                      table: Sequence[List[Cell | None]],
                      combinations: CombsType) -> CellIndex:

        step = cls._find_best_step(symbol, table=table, combinations=combinations)
        print('step: ', step)

        if not isinstance(step[0], int):
            step = random.choice(random.choice(step))

        return step

    @classmethod
    def _find_best_step(cls,
                        symbol,
                        table: Sequence[List[Cell | None]],
                        combinations: CombsType) -> Union[ListCombsType, CellIndex]:

        my_priority_steps = []
        enemy_win_cell = ()

        for combination in combinations:

            count_my_cell = 0
            count_enemy_cell = 0
            count_empty = 0
            empty_cells = []

            for step_comb in combination:
                index_row, index_cell = step_comb
                cell = table[index_row][index_cell]

                if cell is None:
                    count_empty += 1
                    empty_cells.append(step_comb)

                elif cell.symbol == symbol:
                    count_my_cell += 1
                else:
                    count_enemy_cell += 1

            if not count_enemy_cell:  # Only my_cell + empty_cell in combination
                if count_empty == 1:  # One my step left to win this combination
                    return empty_cells[0]

                elif not my_priority_steps or len(my_priority_steps[0]) > count_empty:
                    my_priority_steps = list([empty_cells])

                elif len(my_priority_steps[0]) == count_empty:
                    my_priority_steps.append(empty_cells)

            elif not count_my_cell:  # Only enemy_cell + empty_cell in combination
                if count_empty == 1:  # One enemy step left to win this combination
                    enemy_win_cell = empty_cells[0]

        if enemy_win_cell:
            return enemy_win_cell
        else:
            return my_priority_steps
