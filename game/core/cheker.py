from enum import Enum, verify, UNIQUE
from typing import Optional

from game.core.symbol import Symbol


class CheckerTable:
    @verify(UNIQUE)
    class Cases(Enum):
        CASE_RIGHT = 'index_row, index_cell + temp_index'
        CASE_DOWN = 'index_row + temp_index, index_cell'
        CASE_DOWN_RIGHT = 'index_row + temp_index, index_cell + temp_index'
        CASE_DOWN_LEFT = 'index_row + temp_index, index_cell - temp_index'

    @classmethod
    def check_table_for_player(cls, symbol: Symbol, table: tuple[list], size_combination: int):
        steps_list = cls.find_player_steps(symbol=symbol, table=table)
        result = cls.check_player_steps(size_combination=size_combination, steps_list=steps_list)
        return result

    @classmethod
    def find_player_steps(cls, symbol: Symbol, table: tuple[list]) -> list[tuple]:
        steps_player = []

        for index_row, row in enumerate(table):
            for index_cell, cell in enumerate(row):
                if cell is not None:
                    if cell.symbol == symbol:
                        steps_player.append((index_row, index_cell))

        return steps_player

    @classmethod
    def check_comb(cls, case: Cases, size_combination: int, step: tuple[int, int], steps_list: list[tuple])\
            -> Optional[list[tuple]]:
        """
        Checks each step of the given case for the presence of a winning combination
        :param step: Tuple(index_row, index_cell)
        :return: Winner_combinations: list[(index_row, index_cell), ...] or None
        """
        index_row, index_cell = step
        winner_combination = [step]
        counter = temp_index = 0

        while True:
            temp_index += 1; counter += 1
            expected_step = eval(case.value)

            if counter == size_combination:
                return winner_combination

            if expected_step in steps_list:
                winner_combination.append(expected_step)

            else:
                break

    @classmethod
    def check_player_steps(cls, size_combination: int, steps_list: list[tuple]) -> list[tuple]:
        for step in steps_list:
            for case in cls.Cases:
                win = CheckerTable.check_comb(case, size_combination=size_combination,
                                              step=step, steps_list=steps_list)
                if win:
                    return win
