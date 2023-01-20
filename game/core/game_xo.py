from abc import abstractmethod
from typing import Optional

from game.core.cheker import CheckerDefault, CheckerBase, check_checker_instance
from game.core.players.player import PlayerBase
from game.core.players.players import PlayersBase, verify_players_instance
from game.core.result import ResultCode, GameStateBase, GameState, GameStateT
from game.core.table.annotations import CombType
from game.core.table.table import TableBase, verify_table_instance


class GameBase:
    def __init__(self,
                 players: PlayersBase,
                 table: TableBase,
                 checker: CheckerBase,
                 game_state: GameStateBase):
        verify_players_instance(players)
        verify_table_instance(table)
        check_checker_instance(checker)

        self._players = players
        self._table = table
        self._checker = checker
        self._game_state: GameStateT = game_state
        """Game state. By default, it is indicated that the result is missing. changes as the game progresses"""

    @property
    def game_table(self):
        return self.table.game_table

    @property
    def current_player(self):
        return self._players.current_player

    @property
    def players(self):
        return self._players

    @property
    def table(self):
        return self._table

    @property
    def game_state(self):
        return self._game_state

    def step(self, index_row: int, index_column: int, player: PlayerBase):
        """
        Places a player symbol on the playing field 'self.table'
        * Added symbol in a table
        * Added +1 step in a player.count_step
        * Added this player in current_player
        """
        self.table.set_symbol_cell(index_row=index_row, index_column=index_column, symbol=player.symbol)
        player.add_count_step()

    @abstractmethod
    def result(self, player: PlayerBase) -> GameStateT:
        """
        The function checks the cells of the player given in the argument and returns its result by possible categories:
          - ResultCode.NO_RESULT \n
          - ResultCode.ALL_CELLS_USED \n
          - ResultCode.WINNER \n
        If the ResultCode matches the logical end, calls methods to populate self.game_state. For example:
          - ResultCode.WINNER → self.set_winner,
          - ResultCode.ALL_CELLS_USED → self.set_draw

        Returns ResultCode.
        """
        ...

    def set_winner(self, player: PlayerBase, win_combination: CombType):
        """
        Changes the self._game_state parameter to the result of the game in which there is a winner. \n
        Changes: \n
        * Replaces the result code \n
        * Add a reference to the winning player object \n
        * Add a player winning combination.
        """
        self.game_state.update(code=ResultCode.WINNER, win_player=player, win_combination=win_combination)

    def set_draw(self):
        """
        Changes the self._game_state parameter to the result of a game in which all cells are used and
        there is no winner – i.e., a draw. \n
        Changes: \n
        * Replaces the result code.
        """
        self.game_state.update(code=ResultCode.ALL_CELLS_USED)

    def _win_result(self, player: PlayerBase) -> Optional[CombType]:
        return self._checker.result_player(player.symbol,
                                           table=self.table.game_table,
                                           combinations=self.table.combinations)

    def _draw_result(self) -> bool:
        if self.table.count_free_cells == 0:
            return True


class Game(GameBase):
    def __init__(self,
                 players: PlayersBase,
                 table: TableBase,
                 checker: CheckerBase = CheckerDefault(),
                 game_state: GameStateBase = GameState()):

        super().__init__(players=players, table=table, checker=checker, game_state=game_state)

    def result(self, player: PlayerBase) -> GameStateT:
        if player.count_steps >= self.table.param.COMBINATION:

            if win_comb := self._win_result(player=player):
                self.set_winner(player=player, win_combination=win_comb)

            elif self._draw_result():
                self.set_draw()
        return self.game_state

    def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> GameStateT:
        """
        Sets the symbol for the given player by the given indices and returns its result \n
        This is a unifying function. It includes:\n
        * def self.step
        * def self.result

        :return GameStateT
        """
        self.step(index_row=index_row, index_column=index_column, player=player)
        return self.result(player=player)

    def step_result_next_player(self, index_row: int, index_column: int) -> GameStateT:
        """
        * The symbol of the next player in queue self.players is placed according to the transmitted indices
        * +1 move is added to the player.count_step
        * This player is now available in self.current_player

        This is a unifying function. It includes:\n
        * def self.players.set_next_player
        * def self.step_result → GameStateT

        Warning: if you use self.step or self.step_result
        and pass the argument there players not from the self.players queue,
        but at your discretion, then this method will determine the next player incorrectly,
        and most likely, it will return the first player in the queue.\n
        To avoid this — always use this method, or send players taken from the queue in self.players\n
        Example: self.players.current_player / self.players.set_next_player

        :return GameStateT
        """
        player_now = self.players.set_next_player()
        return self.step_result(index_row=index_row, index_column=index_column, player=player_now)
