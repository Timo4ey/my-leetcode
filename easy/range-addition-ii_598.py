# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return the number of maximum integers in the matrix after performing all the operations.


# Example 1:

# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
# Example 2:

# Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4
# Example 3:

# Input: m = 3, n = 3, ops = []
# Output: 9
# ---------------------------------------Runtime 78 ms Beats 94.32% Memory 18.8 MB Beats 14.77%---------------------------------------


class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if not ops:
            return m * n
        x, y = zip(*ops)
        return min(x) * min(y)
