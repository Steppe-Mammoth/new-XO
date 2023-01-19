import random
from abc import ABC, abstractmethod
from typing import MutableSequence
from itertools import cycle

from game.core.players.player import PlayerBase, CheckPlayers
from game.exceptions.core_exceptions import PlayersInstanceError


class PlayersBase(ABC):
    __slots__ = '_players', '_current_player'

    def __init__(self, players: MutableSequence[PlayerBase]):
        CheckPlayers.list_players(players=players)

        self._players = players
        self._current_player = None

    @property
    def players(self):
        return self._players

    @property
    @abstractmethod
    def current_player(self) -> PlayerBase:
        ...

    @abstractmethod
    def shuffle_players(self):
        """
        Shuffles the list of players and replaces the queue
        Sets the new current player from the updated queue as the current player \n
        available via self.current_player method.
        """
        ...

    @abstractmethod
    def set_next_player(self) -> PlayerBase:
        """
        Replaces the current player with the next player in line and returns it. \n
        New current player available via self.now_player
        """
        ...


class Players(PlayersBase):
    def __init__(self, players: MutableSequence[PlayerBase]):
        super().__init__(players)
        self.__queue = None

    @property
    def current_player(self) -> PlayerBase:
        if not self._current_player:
            self.set_next_player()
        return self._current_player

    def shuffle_players(self):
        random.shuffle(self._players)
        self.__queue = iter(self)
        self.set_next_player()

    def set_next_player(self) -> PlayerBase:
        return next(self)

    def __iter__(self):
        return cycle(self._players)

    def __next__(self) -> PlayerBase:
        if not self.__queue:
            self.__queue = iter(self)

        player = next(self.__queue)
        self._current_player = player
        return player


def check_players_instance(players: PlayersBase):
    if not isinstance(players, PlayersBase):
        raise PlayersInstanceError
