from dataclasses import dataclass


@dataclass(frozen=True)
class TableParam:
    ROW: int
    COLUMN: int
    COMBINATION: int

    def __post_init__(self):
        if self.ROW < self.COMBINATION or self.COLUMN < self.COMBINATION:
            raise ValueError("ROW and COLUMN size must not be less than COMBINATION")
