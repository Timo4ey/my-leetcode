
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false

# ---------------------------------------Runtime 47 ms Beats 35.72% Memory 16.4 MB Beats 7.97%---------------------------------------

# My solution
# Complexity O(n)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        return self.isPowerOfTwo(n/2)