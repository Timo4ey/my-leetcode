# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.


# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0

# ---------------------------------------Runtime 122 ms Beats 71.34% Memory 17.5 MB Beats 5.54%---------------------------------------

from typing import List


# My solution


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        store = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] < 0:
                    store.extend(grid[x][y:])
                    break
        return len(store)
