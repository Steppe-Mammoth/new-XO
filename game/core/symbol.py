from enum import Enum, verify, UNIQUE


@verify(UNIQUE)
class Symbol(Enum):
    X = 1
    O = 0


def symbol_check(symbol: Symbol):
    if not isinstance(symbol, Symbol):
        raise ValueError('Possible only field accessed in Symbol\nExample: Symbol.X')
