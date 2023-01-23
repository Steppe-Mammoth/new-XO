from game import TableParam, TableDefault, GameConsole, Player, Players, Symbol

if __name__ == "__main__":
    p1 = Player(name="ANDROID:1", symbol=Symbol('X'), role=Player.Role.ANDROID)
    p2 = Player(name="ANDROID:4", symbol=Symbol('I'), role=Player.Role.ANDROID)
    p3 = Player(name="ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    p4 = Player(name="PLAYER:2", symbol=Symbol('O'), role=Player.Role.USER)

    players = Players(players=[p1, p2, p3])
    table = TableDefault(param=TableParam(10, 10, 7))

    game = GameConsole(players=players, table=table)
    game.start_game()
