# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

# ---------------------------------------Runtime 37 ms Beats 68.36% Memory 16.1 MB Beats 82.18%---------------------------------------


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        line = [1]
        for i in range(rowIndex):
            line.append(round(line[i] * ((rowIndex - i) / (i + 1))))
        return line
