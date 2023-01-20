import random
from abc import ABC, abstractmethod
from typing import MutableSequence, Sequence
from itertools import cycle

from game.core.players.player import PlayerBase, verify_player_instance, PlayerT
from game.exceptions.core_exceptions import PlayersInstanceError, PlayersIsEmptyError


class PlayersBase(ABC):
    __slots__ = '_player_list', '_current_player'

    def __init__(self, players: MutableSequence[PlayerT]):
        verify_player_list(players=players)

        self._player_list = players
        self._current_player = None

    @property
    def player_list(self):
        return self._player_list

    @property
    @abstractmethod
    def current_player(self) -> PlayerT:
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
    def set_next_player(self) -> PlayerT:
        """
        Replaces the current player with the next player in line and returns it. \n
        New current player available via self.now_player
        """
        ...


class Players(PlayersBase):
    def __init__(self, players: MutableSequence[PlayerT]):
        super().__init__(players)
        self.__queue = None

    @property
    def current_player(self) -> PlayerT:
        if not self._current_player:
            self.set_next_player()
        return self._current_player

    def shuffle_players(self):
        random.shuffle(self._player_list)
        self.__queue = iter(self)
        self.set_next_player()

    def set_next_player(self) -> PlayerT:
        return next(self)

    def __iter__(self):
        return cycle(self._player_list)

    def __next__(self) -> PlayerT:
        if not self.__queue:
            self.__queue = iter(self)

        player = next(self.__queue)
        self._current_player = player
        return player


def verify_players_instance(players: PlayersBase):
    if not isinstance(players, PlayersBase):
        raise PlayersInstanceError


def verify_player_list(players: Sequence[PlayerBase]):
    if len(players) == 0:
        raise PlayersIsEmptyError
    for p in players:
        verify_player_instance(p)
