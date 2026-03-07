# 304. Range Sum Query 2D - Immutable
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a 2D matrix matrix, handle multiple queries of the following type:
#
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            for c in range(COLS):
                self.prefix[r + 1][c + 1] = (
                        matrix[r][c] +
                        self.prefix[r][c + 1] +
                        self.prefix[r + 1][c] -
                        self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 = row2 + 1
        col2 = col2 + 1
        row1 = row1 + 1
        col1 = col1 + 1
        result = (
                self.prefix[row2][col2]
                - self.prefix[row1 - 1][col2]
                - self.prefix[row2][col1 - 1]
                + self.prefix[row1 - 1][col1 - 1]
        )
        return result