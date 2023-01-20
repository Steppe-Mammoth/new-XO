from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, TypeVar, Generic

from game.core.players.player import PlayerBase, verify_player_instance
from game.core.table.annotations import CombType

GameStateT = TypeVar('GameStateT', bound='GameStateBase')


class ResultCode(Enum):
    NO_RESULT = 0
    ALL_CELLS_USED = 1
    WINNER = 2


class GameStateBase(ABC):
    __slots__ = "_code", "_win_player", "_win_combination"

    def __init__(self):
        self._code: ResultCode = ResultCode.NO_RESULT
        self._win_player: Optional[PlayerBase] = None
        self._win_combination: Optional[CombType] = None

    @property
    def code(self) -> ResultCode:
        return self._code

    @property
    def win_player(self) -> Optional[PlayerBase]:
        return self._win_player

    @property
    def win_combination(self) -> Optional[CombType]:
        return self._win_combination

    @abstractmethod
    def update(self,
               code: Optional[ResultCode] = None,
               win_player: Optional[PlayerBase] = None,
               win_combination: Optional[CombType] = None):
        ...


class GameState(GameStateBase):
    def update(self,
               code: Optional[ResultCode] = None,
               win_player: Optional[PlayerBase] = None,
               win_combination: Optional[CombType] = None):

        if code:
            verified_result_code(code)
            self._code = code

        if win_player:
            verify_player_instance(win_player)
            self._win_player = win_player

        if win_combination:
            self._win_combination = win_combination


def verified_result_code(code: ResultCode):
    if not isinstance(code, ResultCode):
        raise AttributeError('Only ResultsCode object ')  # create raise
