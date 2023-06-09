# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.


# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true

# ---------------------------------------Runtime 48 ms Beats 33.13% Memory 16.4 MB Beats 9.18%---------------------------------------

# My solution
# Complexity O(n)


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        return self.isPowerOfFour(n / 4)
