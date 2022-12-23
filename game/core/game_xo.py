from typing import Union, NamedTuple, Optional

from game.core import AI
from game.core.cheker import Checker
from game.core.player import Player
from game.core.symbol import Symbol
from game.core.table.param import TableParam, AllowedTableParameter
from game.core.table.table import Table


class Players(NamedTuple):
    p1: Player
    p2: Player


class GameBase:
    def __init__(self, players: Players, table_param: Union[AllowedTableParameter, TableParam]):
        self.players = players
        self.table = Table(param=table_param)
        print(self)

    def step(self, index_row: int, index_cell: int, symbol: Symbol):
        self.table.set_symbol_cell(index_row=index_row, index_column=index_cell, symbol=symbol)

    def check(self, symbol: Symbol) -> tuple:
        result = Checker.get_result_for_player(symbol, table=self.table.table, combinations=self.table.combinations)
        return result


class Game(GameBase):
    def player_for_symbol(self, symbol: Symbol) -> Player:
        match symbol:
            case self.players.p1.symbol:
                player_now = self.players.p1
            case self.players.p2.symbol:
                player_now = self.players.p2
            case _:
                raise AttributeError

        return player_now

    def step_result(self, index_row: int, index_cell: int, symbol: Symbol) -> tuple:
        super().step(index_row, index_cell=index_cell, symbol=symbol)
        player_now = self.player_for_symbol(symbol)
        player_now.add_step()

        if self.table.param.COMBINATION <= player_now.count_steps:
            print(f"CHECK FOR {player_now.name=} | {player_now.count_steps}")
            return super().check(symbol)


class GamePrintMixin(GameBase):
    def print_players(self):
        p1, p2 = self.players.p1, self.players.p2
        print(f"{p1.name} ({p1.symbol}) VS ({p2.symbol}) {p2.name}")

    def print_table(self):
        print("i: ", end="")
        print('   '.join(str(i) for i in range(len(self.table.table[0]))))
        for index_row, row in enumerate(self.table.table):
            print(index_row, end=": ")
            for index_cell, cell in enumerate(row):
                print(cell.symbol.name if cell is not None else "*", end=" | ")
            print('\n')

    @staticmethod
    def print_check(result: Optional[tuple]):
        if result:
            print(f"WIN | combination info: {result=}")


class GameAI(Game):
    def step_ai(self) -> tuple:
        return AI.FindCellAI.get_best_step(symbol=self.players.p2.symbol,
                                           table=self.table.table,
                                           combinations=self.table.combinations)


class GameConsole(Game, GamePrintMixin):
    def step(self, index_row: int, index_cell: int, symbol: Symbol):
        result = super().step_result(index_row, index_cell=index_cell, symbol=symbol)
        super().print_table()
        super().print_check(result=result)


class GameAIConsole(GameConsole, GameAI):
    def __init__(self, players: Players, table_param: Union[AllowedTableParameter, TableParam]):
        super().__init__(players, table_param)

    def step_ai(self):
        i_row, i_cell = super().step_ai()
        super().step(index_row=i_row, index_cell=i_cell, symbol=self.players.p2.symbol)


print(f"{Table.ONLY_ALLOWED_TABLE_PARAMETERS = }")
p1 = Player(name="PLAYER I", symbol=Symbol.X)
p2 = Player(name="ANDROID II", symbol=Symbol.O)
game = GameAIConsole(players=Players(p1, p2), table_param=TableParam(4, 4, 4))
