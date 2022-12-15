from typing import Union

from game.core.player import Player
from game.core.table.param import TableParam, AllowedTableParameter
from game.core.table.table import Table


class Game:
    def __init__(self, p1: Player, p2: Player, rounds: int, table_param: Union[AllowedTableParameter, TableParam]):
        self.p1: Player = p1
        self.p2: Player = p2
        self._rounds = rounds
        self._table: Table = Table(table_param)

