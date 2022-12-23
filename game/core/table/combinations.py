from enum import verify, UNIQUE, Enum


@verify(UNIQUE)
class Vectors(Enum):
    RIGHT = 'index_row, index_cell + temp_index'
    DOWN = 'index_row + temp_index, index_cell'
    DOWN_RIGHT = 'index_row + temp_index, index_cell + temp_index'
    DOWN_LEFT = 'index_row + temp_index, index_cell - temp_index'


class Combinations:

    @classmethod
    def get_combinations(cls, size_row: int, size_column: int, size_combination=3):
        combinations = []

        for index_row in range(size_row):
            for index_cell in range(size_column):
                for vector in Vectors:
                    comb = cls.get_combination_from_cell(vector=vector,
                                                         step=(index_row, index_cell),
                                                         size_row=size_row,
                                                         size_column=size_column,
                                                         size_combination=size_combination)
                    if comb:
                        combinations.append(comb)

        return combinations

    @classmethod
    def get_combination_from_cell(cls,
                                  vector: Vectors,
                                  step: tuple[int, int],
                                  size_row: int,
                                  size_column: int,
                                  size_combination: int):
        combination = []

        index_row, index_cell = step  # args for eval
        temp_index = size_combination - 1
        expected_index_row, expected_index_cell = eval(vector.value)

        if (0 <= expected_index_row <= size_row - 1) and (0 <= expected_index_cell <= size_column - 1):

            for temp_index in range(size_combination):
                combination.append(eval(vector.value))

            return tuple(combination)
