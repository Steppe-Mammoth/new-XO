from enum import Enum
from abc import ABC, abstractmethod
from functools import lru_cache

from game.core.table.annotations import CombsType, CombType, CellIndex
from game.exceptions.core_exceptions import CombinationsInstanceError
from game.setting import SIZE_CACHE_COMBINATIONS


class Vectors(Enum):
    RIGHT = 'index_row, index_cell + temp_index'
    DOWN = 'index_row + temp_index, index_cell'
    DOWN_RIGHT = 'index_row + temp_index, index_cell + temp_index'
    DOWN_LEFT = 'index_row + temp_index, index_cell - temp_index'


class CombinationsBase(ABC):
    @abstractmethod
    def get_combinations(self, size_row: int,
                         size_column: int,
                         size_combination: int) -> CombsType:
        """
        For the passed arguments of the two-dimensional table, \n
        it finds combinations that will be used to check the winnings for the player, or to find a move for the AI \n
        :param size_row: The number of rows of a two-dimensional table.
        :param size_column: The number of columns of a two-dimensional table.
        :param size_combination: The amount cells filled in a row for a winning result.
        :return: The array is defined in the CombsType annotation.
        """
        ...


class CombDefault(CombinationsBase):
    @classmethod
    @lru_cache(maxsize=SIZE_CACHE_COMBINATIONS)
    def get_combinations(cls, size_row: int, size_column: int, size_combination: int) -> CombsType:
        combinations = []

        for index_row in range(size_row):
            for index_column in range(size_column):
                for vector in Vectors:
                    comb = cls._get_combination_from_cell(vector=vector,
                                                          step=(index_row, index_column),
                                                          size_row=size_row,
                                                          size_column=size_column,
                                                          size_combination=size_combination)
                    if comb:
                        combinations.append(comb)

        combinations = tuple(combinations)
        return combinations

    @classmethod
    def _get_combination_from_cell(cls,
                                   vector: Vectors,
                                   step: tuple[int, int],
                                   size_row: int,
                                   size_column: int,
                                   size_combination: int) -> CombType:
        comb_vector = []

        index_row, index_cell = step  # args for eval
        temp_index = size_combination - 1  # arg for eval
        expected_index_row, expected_index_column = eval(vector.value)  # Кінцеві індекси в векторі

        # Якщо кінцеві індекси в допустимому діапазоні, то комбінація індексів (по вектору) заповнюється
        if (0 <= expected_index_row <= size_row - 1) and (0 <= expected_index_column <= size_column - 1):

            for temp_index in range(size_combination):
                temp_index_cell: CellIndex = eval(vector.value)
                comb_vector.append(temp_index_cell)

            return tuple(comb_vector)


def check_combinations_instance(comb: CombinationsBase):
    if not isinstance(comb, CombinationsBase):
        raise CombinationsInstanceError
