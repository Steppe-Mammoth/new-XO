from dataclasses import dataclass

from game.exceptions.core_exceptions import TableParamInstanceError


@dataclass(frozen=True)
class TableParam:
    ROW: int
    COLUMN: int
    COMBINATION: int

    def __post_init__(self):
        if self.ROW < self.COMBINATION or self.COLUMN < self.COMBINATION:
            raise ValueError("ROW and COLUMN size must not be less than COMBINATION")


def check_table_param_instance(param: TableParam):
    if not isinstance(param, TableParam):
        raise TableParamInstanceError
