from game import TableParam, TableDefault, Player, Players, Symbol
from game.client.console import GameConsole

if __name__ == "__main__":
    p1 = Player(name="PETROS_ANDROID:1", symbol=Symbol('X'), role=Player.Role.ANDROID)
    p2 = Player(name="AMIGOS_ANDROID:2", symbol=Symbol('O'), role=Player.Role.ANDROID)
    p3 = Player(name="GENTOS_ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    # p4 = Player(name="PLAYER", symbol=Symbol('P'), role=Player.Role.USER)  # Якщо без вас ніяк

    players = Players(players=[p1, p2, p3])
    table = TableDefault(param=TableParam(ROW=7, COLUMN=7, COMBINATION=5))

    game = GameConsole(players=players, table=table)
    game.start_game()
