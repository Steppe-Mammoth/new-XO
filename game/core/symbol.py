from enum import Enum, verify, UNIQUE


@verify(UNIQUE)
class Symbol(Enum):
    X = 1
    O = 2

