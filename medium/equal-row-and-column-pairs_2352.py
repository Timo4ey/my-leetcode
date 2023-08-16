# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


# Example 1:

# ￼
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:

# ￼
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

# ---------------------------------------Runtime 576 ms Beats 39.37% Memory 21.3 MB Beats 80.32%---------------------------------------


# Time complexity O(n * m2)
from collections import defaultdict


class Solution:
    def rotateLeft(self, matrix: list[list[int]]):
        height = len(matrix[0])
        width = len(matrix)
        res = []
        for col in range(height):
            res.append([0] * width)
            for row in range(width):
                res[col][width - row - 1] = matrix[row][height - col - 1]
            res[col].reverse()
        return res

    def equalPairs(self, grid: list[list[int]]) -> int:
        counter = 0

        cols = self.rotateLeft(grid)

        for c in cols:
            counter += grid.count(c)

        return counter


# Solution @Armorix


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += m[str(col)]
        return cnt
