class Symbol:
    __slots__ = "name", "value"

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
