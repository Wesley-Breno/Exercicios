class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for column in range(col1, col2 + 1):
                self.rectangle[row][column] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]