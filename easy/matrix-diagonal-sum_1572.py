# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


# Example 1:

# ￼
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:

# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:

# Input: mat = [[5]]
# Output: 5


# ---------------------------------------Runtime 125 ms Beats 41.59% Memory 16.6 MB Beats 77.38%---------------------------------------


class List(list):
    pass


# My solution
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        first = counter = 0
        last = len(mat) - 1
        while first <= last:
            if first != last:
                counter += mat[first][first] + mat[first][last]
                counter += mat[last][first] + mat[last][last]
            else:
                counter += mat[first][first]
            first += 1
            last -= 1
        return counter
