import sys

from game.core.AI import AIFindDefault, AIFindBase
from game.core.game_xo import Game
from game.core.result import ResultCode
from game.core.players.player import PlayerBase
from prettytable import PrettyTable

from game.core.players.players import PlayersBase
from game.core.table.annotations import CellIndex
from game.core.table.table import TableBase
from game.exceptions.core_exceptions import CellAlreadyUsedError, TableIndexError


class GameConsole(Game):
    def __init__(self, players: PlayersBase, table: TableBase, ai: AIFindBase = AIFindDefault()):
        super().__init__(players=players, table=table)
        self.ai = ai

    def get_step_for_player(self, player: PlayerBase) -> CellIndex:
        if player.role == player.Role.ANDROID:
            step = self.ai.get_step(symbol=player.symbol,
                                    table=self.table.table, combinations=self.table.combinations)
        else:
            step = self._get_step_for_user()
        return step

    def _get_step_for_user(self) -> tuple[int]:
        step = None
        while step is None:
            try:
                step = self._input_step_player()
            except ValueError:  # make exception
                print("* Non correct format: Please again\n"
                      "* Enter 2 integer: First for row ↓ index; Second for column → index")
        return step

    @classmethod
    def _input_step_player(cls) -> tuple[int]:
        res = input("ENTER STEP: < ↓ > < → >: ")
        if res == 'exit':
            sys.exit()

        step = tuple(map(int, res.split()))
        if len(step) != 2:
            raise ValueError
        return step

    @classmethod
    def print_step_info(cls, player: PlayerBase, index_row: int, index_column: int):
        print(f'Step taken: {player.name} <{player.symbol.name}> | ↓: {index_row} | →: {index_column}')

    @classmethod
    def print_info_player(cls, player: PlayerBase):
        p = player
        print(f'Player: {p.name} < {p.symbol.name} > | Role: {p.role.name} | Count steps: {p.count_steps}')

    def print_table(self):
        x = PrettyTable()

        x.field_names = ['↓/→'] + [str(i_column) for i_column in range(self.table.param.COLUMN)]
        for i_row, row in enumerate(self.table.table):
            cells_symbols = [cell.symbol.name if cell is not None else "*" for cell in row]
            x.add_row([f"{i_row}:"] + cells_symbols)

        print(x)

    def print_result(self, result: ResultCode):
        match result:
            case ResultCode.WINNER:
                p = self.game_result.win_player
                comb = self.game_result.win_combination
                print(f"WIN: {p.name} < {p.symbol.name } > | COMB: < {comb} >")
            case ResultCode.ALL_CELLS_USED:
                print("PEACE: ALL USED CELLS")

    def start_game(self):
        result = ResultCode.NO_RESULT
        print(f'Start Game | Enter < exit > to quit')

        while result is ResultCode.NO_RESULT:
            p_now = self.players.current_player
            self.print_table()
            self.print_info_player(player=p_now)

            result = None
            i_row = i_column = None

            while result is None:
                i_row, i_column = self.get_step_for_player(player=p_now)
                try:
                    result = self.step_result(index_row=i_row, index_column=i_column, player=p_now)
                except CellAlreadyUsedError:
                    print("This cell is used. Select another cell")
                except TableIndexError:
                    print("This cell is not available, Select another cell")

            self.print_step_info(player=p_now, index_row=i_row, index_column=i_column)
            self.print_result(result)

            if result is ResultCode.NO_RESULT:
                self.players.set_next_player()

        self.print_table()
