from game import TableParam, TableDefault, Player, Players, Symbol, Game
from game.client.console import GameConsole

if __name__ == "__main__":
    p1 = Player(name="ANDROID:1", symbol=Symbol('X'), role=Player.Role.USER)
    p2 = Player(name="ANDROID:4", symbol=Symbol('O'), role=Player.Role.USER)
    p3 = Player(name="ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    p4 = Player(name="PLAYER:2", symbol=Symbol('P'), role=Player.Role.USER)

    players = Players(players=[p1, p2])
    table = TableDefault(param=TableParam(ROW=3, COLUMN=3, COMBINATION=3))

    game = GameConsole(players=players, table=table)
    game.start_game()
