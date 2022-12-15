from game.core.symbol import Symbol


class Checker:

    @classmethod
    def get_result_for_player(cls, symbol: Symbol, table: tuple[list], combinations: list[tuple[tuple]]) -> tuple:
        for combination in combinations:
            count_matches = 0

            for step_comb in combination:
                index_row, index_cell = step_comb
                cell = table[index_row][index_cell]

                if (cell is not None) and (cell.symbol == symbol):
                    count_matches += 1

            if len(combination) == count_matches:
                return combination
