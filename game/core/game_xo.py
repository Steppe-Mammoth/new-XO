from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple, Optional, Tuple
from abc import ABC, abstractmethod

from game.core.cheker import CheckerDefault, CheckerBase
from game.core.players.player import PlayerBase
from game.core.players.players import Players
from game.core.table.annotations import CombType
from game.core.table.table import TableBase


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
