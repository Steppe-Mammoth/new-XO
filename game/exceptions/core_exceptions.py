from game.core.symbol import Symbol
from game.core.table.param import TableParam


class CellAlreadyUsedError(Exception):
    def __init__(self, used_cell: Symbol, new_cell: Symbol):
        self.used_cell = used_cell
        self.new_cell = new_cell

    def __str__(self):
        return f"""
        THIS CELL IS USED. Cell symbol now = {self.used_cell.name}, you send = {self.new_cell.name}
        """


class TableIndexError(Exception):
    def __init__(self, index_column: int, index_row: int, table_param: TableParam):
        self.index_column = index_column
        self.index_row = index_row
        self.table_param = table_param

    def __str__(self):
        return f"""
        NOT ALLOWED INDEX for setting symbol in table
        INDEX_COLUMN: You send <{self.index_column}> | Possible: MAX <{self.table_param.COLUMN - 1}> MIN <0> index.
        INDEX_ROW: You send <{self.index_row}> | Possible: MAX <{self.table_param.ROW - 1}> MIN <0> index.
        """


class TableParametersError(Exception):
    def __str__(self):
        return """
        This parameters is not supported
        
        If ONLY_ALLOWED_TABLE_PARAMETERS = True:
        - Send only parameters set in "AllowedTableParameter"
        - Example: Table(AllowedTableParameter.DEFAULT)
        
        If ONLY_ALLOWED_TABLE_PARAMETERS = False:
        - Create user parameter used "TableParam"
        """


class SymbolError(Exception):
    def __str__(self):
        return """
        Possible only field accessed in Symbol. 
        - Example: Symbol.X'
        """