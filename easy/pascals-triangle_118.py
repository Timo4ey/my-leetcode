# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

# ---------------------------------------Runtime 45 ms Beats 40.33% Memory 16.1 MB Beats 94.68%---------------------------------------


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        output = []
        for i in range(numRows):
            row = [1] * (1 + i)
            for j in range(i + 1):
                if j != 0 and i != j:
                    row[j] = output[i - 1][j - 1] + output[i - 1][j]
            output.append(row)
        return output
