# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

# ---------------------------------------Runtime 70 ms Beats 78.22% Memory 17.2 MB Beats 53.19%---------------------------------------
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = [[None] * rows for _ in range(cols)]

        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                res[c][r] = col
        return res
