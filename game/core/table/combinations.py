from enum import verify, UNIQUE, Enum


@verify(UNIQUE)
class Cases(Enum):
    CASE_RIGHT = 'index_row, index_cell + temp_index'
    CASE_DOWN = 'index_row + temp_index, index_cell'
    CASE_DOWN_RIGHT = 'index_row + temp_index, index_cell + temp_index'
    CASE_DOWN_LEFT = 'index_row + temp_index, index_cell - temp_index'


class Combinations:

    @classmethod
    def get_combinations(cls, size_row: int, size_column: int, size_combination=3):
        combinations = []

        for index_row in range(size_row):
            for index_cell in range(size_column):
                for case in Cases:
                    comb = cls.get_combination_from_cell(case=case,
                                                         step=(index_row, index_cell),
                                                         size_row=size_row,
                                                         size_column=size_column,
                                                         size_combination=size_combination)
                    if comb:
                        combinations.append(comb)

        return combinations

    @classmethod
    def get_combination_from_cell(cls,
                                  case: Cases,
                                  step: tuple[int, int],
                                  size_row: int,
                                  size_column: int,
                                  size_combination: int):
        combination = []

        index_row, index_cell = step  # args for eval(case.value)
        temp_index = size_combination - 1
        expected_index_row, expected_index_cell = eval(case.value)

        if (0 <= expected_index_row <= size_row - 1) and (0 <= expected_index_cell <= size_column - 1):

            for temp_index in range(size_combination):
                combination.append(eval(case.value))

            return tuple(combination)
