from abc import ABC, abstractmethod
from typing import Iterable

from game.core.players.player import PlayerBase, Player
from game.core.symbol import Symbol


class PlayersBase(ABC):
    __slots__ = '_players', '_now_player'

    def __init__(self, players: Iterable[PlayerBase]):
        self._players = []
        self._now_player: PlayerBase | None = None
        self.add_players(players)

    @abstractmethod
    def add_players(self, players: Iterable[PlayerBase]):  # add test
        self._players += players

    @property
    def players(self):
        return self._players  # add test

    @property
    @abstractmethod
    def now_player(self) -> PlayerBase:
        pass

    @abstractmethod
    def get_next_player(self) -> PlayerBase:  # add test
        pass

    @abstractmethod
    def set_now_player(self, player: PlayerBase):  # add test
        self._now_player = player


class Players(PlayersBase):
    def __init__(self, players: Iterable[PlayerBase]):
        super().__init__(players)
        self._deque_p = None

    def add_players(self, players: Iterable[PlayerBase]):  # Добавить списком
        for player in players:
            if not isinstance(player, PlayerBase):
                raise ValueError('Only Player')  # Зробить виключення
        super().add_players(players)

    @property
    def now_player(self) -> PlayerBase:
        if not self._now_player:
            if len(self._players) > 0:
                self.set_now_player(self._players[0])
            else:
                raise AttributeError("First added players. self.players is empty")  # Зробить виключення 1
        return self._now_player

    def set_now_player(self, player: PlayerBase):
        if not isinstance(player, PlayerBase):
            raise ValueError('Only Player')  # Зробить виключення

        super().set_now_player(player)

    def get_next_player(self) -> PlayerBase:
        if len(self._players) == 0:
            raise AttributeError('First added players. self.players is empty')  # Зробить виключення 2  # add test

        if not self._deque_p:
            self._deque_p = self._deque_players()
            self._deque_p.send(None)

        return next(self._deque_p)

    def _deque_players(self):
        while True:
            for player in self._players:
                yield player


p1 = Player('Igor1', Symbol('X', 1))
p2 = Player('Igor2', Symbol('O', 2))

p = Players(players=(p1, p2))
