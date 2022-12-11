from game.core.symbol import Symbol, symbol_check


class Player:
    def __new__(cls, name, symbol):
        symbol_check(symbol)
        instance = super().__new__(cls)
        return instance

    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol
        self.count_steps = 0


