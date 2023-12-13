# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).


# Example 1:

# ￼
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:

# ￼
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

# ---------------------------------------Runtime 8285 ms Beats 5.50% Memory 17.9 MB Beats 5.50%---------------------------------------

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        seen = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    seen.add((i, j))

        to_discard = set()
        for s in seen:
            for s2 in seen:
                if s == s2:
                    continue
                if s[0] == s2[0] or s[1] == s2[1]:
                    to_discard.add(s2)
        return len(seen) - len(to_discard)
