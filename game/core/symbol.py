from game.exceptions.core_exceptions import SymbolError


class Symbol:
    __slots__ = "name"

    def __init__(self, name: str):
        self.name = name


def check_symbol(symbol):
    if not isinstance(symbol, Symbol):
        raise SymbolError
