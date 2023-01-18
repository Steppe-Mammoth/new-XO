from abc import ABC, abstractmethod
from typing import Optional, Sequence, Generator

from game.core.players.player import PlayerBase, CheckPlayers
from game.exceptions.core_exceptions import PlayersInstanceError


class PlayersBase(ABC):
    __slots__ = '_players', '_now_player'

    def __init__(self, players: Sequence[PlayerBase]):
        CheckPlayers.list_players(players=players)

        self._players = players
        self._now_player: Optional[PlayerBase] = None

    def set_now_player(self, player: PlayerBase):  # add test
        CheckPlayers.player_instance(player=player)
        self._now_player = player

    @property
    def players(self):
        return self._players  # add test

    @property
    @abstractmethod
    def now_player(self) -> PlayerBase:
        return self._now_player

    @abstractmethod
    def get_next_player(self) -> PlayerBase:  # add test
        pass


class Players(PlayersBase):
    def __init__(self, players: Sequence[PlayerBase]):
        super().__init__(players)

        self._deque_players = None

    @property
    def now_player(self) -> PlayerBase:
        if not self._now_player:
            super().set_now_player(self._players[0])
        return self._now_player

    def get_next_player(self) -> PlayerBase:
        if not self._deque_players:
            self._deque_players = self._deque_for_players()
            self._deque_players.send(None)

        return next(self._deque_players)

    def _deque_for_players(self) -> Generator:
        while True:
            for player in self._players:
                yield player


def check_players_instance(players: PlayersBase):
    if not isinstance(players, PlayersBase):
        raise PlayersInstanceError
