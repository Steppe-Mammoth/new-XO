from typing import List, Sequence, Optional
from abc import ABC, abstractmethod

from game.core.symbol import Symbol
from game.core.table.annotations import CombType, CombsType
from game.core.table.cell import Cell
from game.exceptions.core_exceptions import CheckerInstanceError


class CheckerBase(ABC):
    @abstractmethod
    def result_player(self, symbol: Symbol,
                      table: Sequence[List[Cell | None]],
                      combinations: CombsType) -> Optional[CombType]:
        """
        :param symbol:
        :param table:
        :param combinations:
        :return: ((index_row: int ,index_cell: int), ...) if Winner / else None.
        """
        pass


class CheckerDefault(CheckerBase):

    @classmethod
    def result_player(cls, symbol: Symbol,
                      table: Sequence[List[Cell | None]],
                      combinations: CombsType) -> Optional[CombType]:

        for combination in combinations:
            count_matches = 0

            for step in combination:  # Для кожної комбінації в списку комбінацій, проходить по клітці комбінації
                index_row, index_column = step
                cell = table[index_row][index_column]

                if (cell is not None) and (cell.symbol == symbol):  # Якщо клітинка належить переданому символу
                    count_matches += 1

            if len(combination) == count_matches:
                win_comb = combination  # ((0, 0), (0, 1), (0, 2))
                return win_comb


def check_checker_instance(checker: CheckerBase):
    if not isinstance(checker, CheckerBase):
        raise CheckerInstanceError
