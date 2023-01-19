from game.exceptions.core_exceptions import SymbolError


class SymbolBase:
    __slots__ = "name"

    def __init__(self, name: str):
        self.name = name


def check_symbol(symbol):
    if not isinstance(symbol, SymbolBase):
        raise SymbolError
