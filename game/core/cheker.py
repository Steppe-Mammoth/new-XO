from typing import List, Sequence, Optional
from abc import ABC, abstractmethod

from game.core.symbol import SymbolBase
from game.core.table.annotations import CombType, CombsType
from game.core.table.cell import Cell
from game.exceptions.core_exceptions import CheckerInstanceError


class CheckerBase(ABC):
    @abstractmethod
    def result_player(self, symbol: SymbolBase,
                      table: Sequence[List[Cell | None]],
                      combinations: CombsType) -> Optional[CombType]:
        """
        The function checks in the given table for matches of the given symbol
        in each combination in the combinations given by the argument.\n
        If it exists – returns the winning combination for the transmitted symbol.
        """
        ...


class CheckerDefault(CheckerBase):

    @classmethod
    def result_player(cls, symbol: SymbolBase,
                      table: Sequence[List[Cell | None]],
                      combinations: CombsType) -> Optional[CombType]:

        for combination in combinations:
            count_matches = 0

            for index_row, index_column in combination:
                cell = table[index_row][index_column]

                if (cell is not None) and (cell.symbol == symbol):  # cell has an identical symbol
                    count_matches += 1

            if len(combination) == count_matches:
                win_comb = combination  # ((0, 0), (0, 1), (0, 2))
                return win_comb


def check_checker_instance(checker: CheckerBase):
    if not isinstance(checker, CheckerBase):
        raise CheckerInstanceError
