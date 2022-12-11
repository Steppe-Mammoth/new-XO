from game.core.symbol import Symbol, symbol_check


class CellMeta:
    def __new__(cls, symbol):
        symbol_check(symbol)
        instance = super().__new__(cls)
        return instance

    def __deepcopy__(self, memo):
        return self


class Cell(CellMeta):
    def __init__(self, symbol: Symbol):
        self.__symbol = symbol

    @property
    def symbol(self) -> Symbol:
        return self.__symbol
