from game import TableParam, TableDefault, GameConsole, Player, Players, SymbolBase

p1 = Player(name="ANDROID:1", symbol=SymbolBase('X'), role=Player.Role.ANDROID)
p2 = Player(name="ANDROID:4", symbol=SymbolBase('I'), role=Player.Role.ANDROID)
p3 = Player(name="ANDROID:3", symbol=SymbolBase('K'), role=Player.Role.ANDROID)

p4 = Player(name="PLAYER:2", symbol=SymbolBase('O'), role=Player.Role.USER)

players = Players(players=[p1, p2, p3, p4])
table = TableDefault(param=TableParam(5, 5, 4))

game = GameConsole(players=players, table=table)
game.start_game()
