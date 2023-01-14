from time import sleep

from game.core.AI import AIFindDefault
from game.core.game_xo import Game, ResultCode
from game.core.players.player import PlayerBase


class GameConsole(Game):
    def print_table(self):
        print("i: ", end="")
        print('   '.join(str(i) for i in range(len(self.table.table[0]))))
        for index_row, row in enumerate(self.table.table):
            print(index_row, end=": ")
            for index_column, cell in enumerate(row):
                print(cell.symbol.name if cell is not None else "*", end=" | ")
            print('\n')

    def print_result(self, result: ResultCode):
        match result:
            case ResultCode.WINNER:
                r = self.result_game.value
                print(f"WIN -> NAME: {r.player.name} | COMB: {r.combinations}")
            case ResultCode.ALL_CELLS_USED:
                print("PEACE: ALL USED CELLS")
            case _:
                print('OK. NEXT ...')

    def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> ResultCode:
        result = super().step_result(index_row=index_row, index_column=index_column, player=player)
        return result

    def start_game(self):
        result = ResultCode.NO_RESULT

        print(f'Start Game')
        while result is ResultCode.NO_RESULT:
            p_now = self.players.now_player
            self.print_table()
            print(f'** STEP FOR: {p_now.name}')

            if p_now.role == p_now.Role.ANDROID:
                sleep(2)
                i_r, i_c = AIFindDefault.get_best_step(symbol=p_now.symbol,
                                                       table=self.table.table,
                                                       combinations=self.table.combinations)
            else:
                i_r, i_c = map(int, input("Який ваш хід? (<index row> <index column>): ").split())

            result = self.step_result(index_row=i_r, index_column=i_c, player=p_now)
            self.print_result(result)

            if result is ResultCode.NO_RESULT:
                p_next = self.players.get_next_player()
                self.players.set_now_player(p_next)

        self.print_table()
