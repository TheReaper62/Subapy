from __future__ import annotations

__all__ = (
    'Filter',
)

class Filter:
    """
    This class is used to add (a) filter(s) to a query.
    Example: Select rows that has a age value greater than equals to 18.
    Code: Filter('age', 'gte', '18') or Filter('institute','wfts(english).jc')
    """
    def __init__(self, *args: list[str], raw:bool = False):
        col:str
        op:str
        query:str
        self.filter: dict[str,str]
        # Raw
        if raw and len(args) == 1:
             self.raw:bool = True
             self.value = args[0]
        # Basic
        elif len(args) == 3:
            col = args[0]
            op = args[1]
            query = args[2]
            self.filter = {col : f"{op}.{query}"}
        # Complex
        elif len(args) == 1:
            col, query = args.split("=")
            self.filter = {col : query}
        elif len(args) == 2:
            col = args[0]
            query = args[1]
            self.filter = {col : query}
        else:
            raise KeyError("Invalid number of arguments for filter")

    def __add__(self, other):
        if isinstance(other, Filter):
            if self.raw or other.raw:
                raise TypeError("Unsupported operand type for +, when one of the Filter objects is raw")
            else:
                return Filter(self.filter | other.filter)
        else:
            raise TypeError("Unsupported operand type for +")

    def __radd__(self, other):
        if isinstance(other, Filter):
            if self.raw or other.raw:
                raise TypeError("Unsupported operand type for +, when one of the Filter objects is raw")
            else:
                return Filter(self.filter | other.filter)
        else:
            raise TypeError("Unsupported operand type for +")
