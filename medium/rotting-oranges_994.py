# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Example 1:

# ￼
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# ---------------------------------------Runtime 63 ms Beats 27.19% Memory 16.3 MB Beats 56.30%---------------------------------------


from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        cols = len(grid[0])
        rows = len(grid)
        time = fresh = 0

        # counting fresh oranges and add rotten orange in q
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        # direction for checking if orange has a neighbor
        directions = set({(0, 1), (0, -1), (1, 0), (-1, 0)})

        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row < 0
                        or row == rows
                        or col < 0
                        or col == cols
                        or grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
