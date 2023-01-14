from dataclasses import dataclass
from enum import Enum
from time import sleep
from typing import NamedTuple, Optional, Tuple
from abc import ABC, abstractmethod

from game.core.AI import AIFindDefault
from game.core.cheker import CheckerDefault, CheckerBase
from game.core.players.player import Player, PlayerBase
from game.core.players.players import Players
from game.core.symbol import Symbol
from game.core.table.annotations import CombType
from game.core.table.param import TableParam
from game.core.table.table import TableDefault, TableBase


class ResultCode(Enum):
    NO_RESULT = 0
    ALL_CELLS_USED = 1
    WINNER = 2


class WinnerInfo(NamedTuple):
    player: PlayerBase
    combinations: CombType


@dataclass(frozen=True)
class Result:
    code: ResultCode
    value: Optional[WinnerInfo] = None

    def __post_init__(self):
        if type(self.code) is not ResultCode:
            raise AttributeError('Only ResultsCode object ')

        if self.code == ResultCode.WINNER:
            if not isinstance(self.value, WinnerInfo):
                raise AttributeError('WinnerInfo only')


class GameBase(ABC):
    def __init__(self, players: Players, checker: CheckerBase, table: TableBase):
        self.checker = checker
        self.players = players
        self.table = table

        self._result_game: Optional[Result] = None

    @property
    def result_game(self) -> Result:
        return ResultCode.NO_RESULT if not self._result_game else self._result_game

    @abstractmethod
    def step(self, index_row: int, index_column: int, player: PlayerBase):
        self.table.set_symbol_cell(index_row=index_row, index_column=index_column, symbol=player.symbol)

    @abstractmethod
    def result(self, player: PlayerBase) -> Tuple[Tuple[int, int]] | ResultCode:
        return self.checker.result_player(symbol=player.symbol,
                                          table=self.table.table,
                                          combinations=self.table.combinations)


class Game(GameBase):
    def __init__(self, players: Players, table: TableBase, checker: CheckerBase = CheckerDefault()):
        super().__init__(players, checker, table)

    def step(self, index_row: int, index_column: int, player: PlayerBase):
        super().step(index_row=index_row, index_column=index_column, player=player)
        player.add_count_step()

    def result(self, player: PlayerBase) -> ResultCode:
        result_code = ResultCode.NO_RESULT

        if self.table.param.COMBINATION <= player.count_steps:
            print(f"CHECK FOR {player.name=} | count_steps: {player.count_steps}")

            if win_comb := super().result(player=player):
                result_code = ResultCode.WINNER
                result = Result(result_code, value=WinnerInfo(player=player, combinations=win_comb))
                self._result_game = result

            elif self.table.count_free_cells == 0:
                result_code = ResultCode.ALL_CELLS_USED
                self._result_game = Result(result_code)

        return result_code

    def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> ResultCode:
        self.step(index_row=index_row, index_column=index_column, player=player)
        return self.result(player=player)


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



p1 = Player(name="1 ANDROID 1", symbol=Symbol('X', 1), role=Player.Role.ANDROID)
p2 = Player(name="2 PLAYER 2", symbol=Symbol('O', 2), role=Player.Role.USER)
# p3 = Player(name="3 ANDROID 3", symbol=Symbol('K', 3), role=Player.Role.ANDROID)
# p4 = Player(name="4 ANDROID 4", symbol=Symbol('i', 4), role=Player.Role.ANDROID)

p = Players(players=[p1, p2])

t = TableDefault(param=TableParam(4, 4, 4))

game = GameConsole(players=p, table=t)
game.start_game()
