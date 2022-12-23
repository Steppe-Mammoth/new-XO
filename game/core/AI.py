import random
from game.core.table.cell import Cell


class FindCellAI:
    @classmethod
    def get_best_step(cls, symbol, table: list[tuple[Cell]], combinations: list[tuple[tuple]]) -> tuple:
        step = cls.find_best_step(symbol, table=table, combinations=combinations)

        if not isinstance(step[0], int):
            step = random.choice(random.choice(step))

        return step

    @classmethod
    def find_best_step(cls, symbol, table: list[tuple[Cell]], combinations: list[tuple[tuple]]):
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
