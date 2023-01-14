from game.client.console import GameConsole
from game.core.players.player import Player
from game.core.players.players import Players
from game.core.symbol import Symbol
from game.core.table.param import TableParam
from game.core.table.table import TableDefault

p1 = Player(name="1 ANDROID 1", symbol=Symbol('X', 1), role=Player.Role.ANDROID)
p2 = Player(name="2 PLAYER 2", symbol=Symbol('O', 2), role=Player.Role.USER)
# p3 = Player(name="3 ANDROID 3", symbol=Symbol('K', 3), role=Player.Role.ANDROID)
# p4 = Player(name="4 ANDROID 4", symbol=Symbol('i', 4), role=Player.Role.ANDROID)

p = Players(players=[p1, p2])

t = TableDefault(param=TableParam(4, 4, 4))

game = GameConsole(players=p, table=t)
game.start_game()