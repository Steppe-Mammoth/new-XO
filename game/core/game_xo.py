from typing import Optional

from game.core.cheker import CheckerDefault, CheckerBase, check_checker_instance
from game.core.players.player import PlayerBase
from game.core.players.players import PlayersBase, check_players_instance
from game.core.result import ResultCode, GameStateBase, GameState
from game.core.table.annotations import CombType
from game.core.table.table import TableBase, check_table_instance


class GameBase:
    def __init__(self, players: PlayersBase, table: TableBase, checker: CheckerBase):
        check_players_instance(players)
        check_table_instance(table)
        check_checker_instance(checker)

        self._players = players
        self._table = table
        self._checker = checker
        self._game_state: GameState = GameState(code=ResultCode.NO_RESULT)
        """Game state. By default, it is indicated that the result is missing. changes as the game progresses"""

    @property
    def players(self):
        return self._players

    @property
    def table(self):
        return self._table

    @property
    def game_result(self) -> GameState:
        return self._game_state

    def step(self, index_row: int, index_column: int, player: PlayerBase):
        """
        Places a player symbol on the playing field 'self.table'
        """
        self.table.set_symbol_cell(index_row=index_row, index_column=index_column, symbol=player.symbol)

    def result(self, player: PlayerBase) -> ResultCode:
        """
        Function return object ResultCode for the player passed in the argument
        If the ResultCode corresponds to the logical end of the game (for example,
        ResultCode.WINNER, ResultCode.ALL_CELLS_USED),
        then the function automatically changes the 'game_result' attribute,
        adding final changes to it depending on the result of the game.
        """

        if win_comb := self._player_result(player=player):
            self.set_winner(player=player, win_combination=win_comb)

        elif self._table_result():
            self.set_draw()

        return self.game_result.code

    def _player_result(self, player: PlayerBase) -> Optional[CombType]:
        return self._checker.result_player(player.symbol, table=self.table.table, combinations=self.table.combinations)

    def _table_result(self) -> bool:
        if self.table.count_free_cells == 0:
            return True

    def set_winner(self, player: PlayerBase, win_combination: CombType):
        """
        Changes the self._game_state parameter to the result of the game in which there is a winner. \n
        Changes: \n
        * Replaces the result code \n
        * Add a reference to the winning player object \n
        * Add a player winning combination.
        """
        self.game_result.update(code=ResultCode.WINNER, win_player=player, win_combination=win_combination)

    def set_draw(self):
        """
        Changes the self._game_state parameter to the result of a game in which all cells are used and
        there is no winner – i.e., a draw. \n
        Changes: \n
        * Replaces the result code.
        """
        self.game_result.update(code=ResultCode.ALL_CELLS_USED)


class Game(GameBase):
    def __init__(self, players: PlayersBase, table: TableBase, checker: CheckerBase = CheckerDefault()):
        super().__init__(players=players, table=table, checker=checker)

    def step(self, index_row: int, index_column: int, player: PlayerBase):
        super().step(index_row=index_row, index_column=index_column, player=player)
        player.add_count_step()

    def result(self, player: PlayerBase) -> ResultCode:
        result = ResultCode.NO_RESULT

        if self.table.param.COMBINATION <= player.count_steps:
            result = super().result(player=player)
        return result

    def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> ResultCode:
        """
        Unifying function. Includes the following functions:\n
        * def self.step
        * def self.result
        """
        self.step(index_row=index_row, index_column=index_column, player=player)
        return self.result(player=player)
