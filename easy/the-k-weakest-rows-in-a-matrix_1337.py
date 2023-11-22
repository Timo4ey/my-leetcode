# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
# The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.


# Example 1:

# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]
# Explanation:
# The number of soldiers in each row is:
# - Row 0: 2
# - Row 1: 4
# - Row 2: 1
# - Row 3: 2
# - Row 4: 5
# The rows ordered from weakest to strongest are [2,0,3,1,4].
# Example 2:

# Input: mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2
# Output: [0,2]
# Explanation:
# The number of soldiers in each row is:
# - Row 0: 1
# - Row 1: 4
# - Row 2: 1
# - Row 3: 1
# The rows ordered from weakest to strongest are [0,2,3,1].


# ---------------------------------------Runtime 116 ms Beats 61.79% Memory 16.8 MB Beats 20.83%---------------------------------------
from typing import List

# My Solution
# The time complexity of this code is O(mn log k),
# where m is the number of rows,
# n is the number of columns, and k is the number of weakest rows to return.


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans: List[int] = []
        tmp: List[tuple(int, int)] = []
        for i, m in enumerate(mat):
            tmp.append((i, sum(m)))
        tmp.sort(key=lambda x: x[1])
        ans = [x[0] for x in tmp]
        return ans[:k]


# Solution @C0R3
# Time complexity: O(m * (n + log m))
# Space complexity: O(m)
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]
