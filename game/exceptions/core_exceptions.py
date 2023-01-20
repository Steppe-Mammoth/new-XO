class CellAlreadyUsedError(Exception):
    def __init__(self, used_symbol: str, new_symbol: str):
        self.used_cell = used_symbol
        self.new_cell = new_symbol

    def __str__(self):
        return f"""
        THIS CELL IS USED. Cell symbol now = {self.used_cell}, you send = {self.new_cell}
        """


class AllCellsUsedError(Exception):
    def __init__(self, game_table):
        self.game_table = game_table

    def __str__(self):
        print_table = '\n'.join([str(row) for row in self.game_table])
        return f"""
        The table is completely filled, there are no free cells left
        Result:{print_table}
        """


class TableIndexError(Exception):
    def __init__(self, index_column, index_row, table_param):
        self.index_column = index_column
        self.index_row = index_row
        self.table_param = table_param

    def __str__(self):
        return f"""
        NOT ALLOWED INDEX for setting symbol in table
        INDEX_COLUMN: You send <{self.index_column}> | Possible: MAX <{self.table_param.COLUMN - 1}> MIN <0> index.
        INDEX_ROW: You send <{self.index_row}> | Possible: MAX <{self.table_param.ROW - 1}> MIN <0> index.
        """


class TableParamInstanceError(Exception):
    def __str__(self):
        return """
        - Create user parameter used class "TableParam"
        """


class TableInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect Table class object. Pass table object that are descendants of the TableBase class
        """


class SymbolError(Exception):
    def __str__(self):
        return """
        Possible only Symbol objects. 
        - Example: Symbol(name='X')
        """


class PlayersIsEmptyError(Exception):
    def __str__(self):
        return """
        The list of players is empty. Add players: Sequence[PlayerBase] first to start the game
        """


class BadRoleError(Exception):
    def __str__(self):
        return """
        Incorrect player role. Pass the roles listed in the PlayerBase.Role class as an argument
        - Example: PlayerBase.Role.User
        """


class PlayerInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect Player class object. Pass player that are descendants of the PlayerBase class
        """


class PlayersInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect Players class object. Pass players object that are descendants of the PlayersBase class
        """


class CheckerInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect Checker class object. Pass checker object that are descendants of the CheckerBase class
        """


class CombinationsInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect Combinations class object. Pass Combinations object that are descendants of the CombinationsBase class
        """