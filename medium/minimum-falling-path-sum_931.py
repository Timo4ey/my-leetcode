# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


# Example 1:

# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:

# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.


# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100


# ---------------------------------------Runtime 148 ms Beats 36.19% Memory 26.87 MB Beats 10.06%---------------------------------------

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        res = max_value = float("inf")
        m_cache = {}

        def dfs(r, c):
            if r == N:
                return 0
            if c < 0 or c == N:
                return max_value
            if (r, c) in m_cache:
                return m_cache[(r, c)]
            res = matrix[r][c] + min(
                dfs(r + 1, c - 1), dfs(r + 1, c), dfs(r + 1, c + 1)
            )
            m_cache[(r, c)] = res
            return res

        for c in range(N):
            res = min(res, dfs(0, c))

        return res
