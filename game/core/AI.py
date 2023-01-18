import random
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Sequence, NamedTuple

from game.core.symbol import Symbol
from game.core.table.annotations import CellIndex, CombsType
from game.core.table.cell import Cell


ListCombsType = List[List[CellIndex]]


class AIResultCode(Enum):
    BestCell = 1
    BestCombs = 2
    EmptyCells = 3


class AIResult(NamedTuple):
    result_code: AIResultCode
    value: Sequence


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

        cell_index = None
        result = cls._find_best_step(symbol, table=table, combinations=combinations)

        match result.result_code:
            case AIResultCode.BestCell:
                cell_index = result.value
            case AIResultCode.BestCombs:
                cell_index = random.choice(random.choice(result.value))
            case AIResultCode.EmptyCells:
                cell_index = random.choice(result.value)

        return cell_index

    @classmethod
    def _find_best_step(cls, symbol, table: Sequence[List[Cell | None]], combinations: CombsType) -> AIResult:

        result_code = None
        value = None

        my_priority_steps = []
        enemy_win_cell = ()
        empty_cells = set()

        for combination in combinations:

            count_my_cell_in_comb = 0
            count_enemy_cell_in_comb = 0
            count_empty_in_comb = 0
            empty_cells_in_comb = []

            for step_comb in combination:
                index_row, index_column = step_comb
                cell = table[index_row][index_column]

                if cell is None:
                    count_empty_in_comb += 1
                    empty_cells_in_comb.append(step_comb)

                elif cell.symbol == symbol:
                    count_my_cell_in_comb += 1
                else:
                    count_enemy_cell_in_comb += 1

            if count_enemy_cell_in_comb == 0:  # Only my_cell + empty_cell in combination
                if count_empty_in_comb == 1:  # One my step left to win this combination
                    result_code = AIResultCode.BestCell
                    value = empty_cells_in_comb[0]
                    break

                elif not my_priority_steps or len(my_priority_steps[0]) > count_empty_in_comb:
                    my_priority_steps = list([empty_cells_in_comb])

                elif len(my_priority_steps[0]) == count_empty_in_comb:
                    my_priority_steps.append(empty_cells_in_comb)

            elif count_my_cell_in_comb == 0:  # Only enemy_cell + empty_cell in combination
                if count_empty_in_comb == 1:  # One enemy step left to win this combination
                    enemy_win_cell = empty_cells_in_comb[0]

            else:
                empty_cells.update(empty_cells_in_comb)

        if result_code and value:
            pass

        elif enemy_win_cell:
            result_code = AIResultCode.BestCell
            value = enemy_win_cell

        elif my_priority_steps:
            result_code = AIResultCode.BestCombs
            value = my_priority_steps
        else:
            result_code = AIResultCode.EmptyCells
            value = tuple(empty_cells)

        return AIResult(result_code=result_code, value=value)
