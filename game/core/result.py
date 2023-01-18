from abc import ABC, abstractmethod
from enum import Enum

from game.core.players.player import PlayerBase
from game.core.table.annotations import CombType


class ResultCode(Enum):
    NO_RESULT = 0
    ALL_CELLS_USED = 1
    WINNER = 2


class ResultBase(ABC):
    __slots__ = "_code", "_win_player", "_win_combination"

    def __init__(self, code: ResultCode, win_player: PlayerBase = None, win_combination: CombType = None):
        self._code = None
        self._win_player = None
        self._win_combination = None

        self.update(code=code, win_player=win_player, win_combination=win_combination)

    @abstractmethod
    def update(self, code: ResultCode = None, win_player: PlayerBase = None, win_combination: CombType = None):
        if code:
            self.code = code
        if win_player:
            self.win_player = win_player
        if win_combination:
            self.win_combination = win_combination

    @property
    def code(self) -> ResultCode:
        return self._code

    @property
    def win_player(self) -> PlayerBase:
        return self._win_player

    @property
    def win_combination(self) -> CombType:
        return self._win_combination

    @code.setter
    def code(self, code: ResultCode):
        if type(code) is not ResultCode:
            raise AttributeError('Only ResultsCode object ')  # create raise
        self._code = code

    @win_player.setter
    def win_player(self, player: PlayerBase):
        if not isinstance(player, PlayerBase):
            raise AttributeError('PlayerBase only')  # create raise
        self._win_player = player

    @win_combination.setter
    def win_combination(self, comb: CombType):
        self._win_combination = comb


class Result(ResultBase):
    def __init__(self, code: ResultCode, win_player: PlayerBase = None, win_combination: CombType = None):
        super().__init__(code=code, win_player=win_player, win_combination=win_combination)

    def update(self, code: ResultCode = None, win_player: PlayerBase = None, win_combination: CombType = None):
        super().update(code=code, win_player=win_player, win_combination=win_combination)
