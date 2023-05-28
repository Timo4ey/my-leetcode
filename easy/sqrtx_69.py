# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned

# ---------------------------------------Runtime 67 ms Beats 26.42% Memory 16.5 MB Beats 7.8%---------------------------------------

# My Solution
# Time Complexity O(log n)
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            middle = (start + end) // 2
            guess = int(math.sqrt(x))
            if middle == guess:
                return guess
            if middle > guess:
                end = middle - 1
            elif middle < guess:
                start = middle + 1


# ---------------------------------------Runtime 52 ms Beats 26.42% Memory 16.5 MB Beats 7.8%---------------------------------------

# Solution  @OldCodingFarmer
# Time Complexity O(log n)

class Solution1:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            middle = (start + end) // 2
            guess = int(math.sqrt(x))
            if middle == guess:
                return guess
            if middle > guess:
                end = middle - 1
            elif middle < guess:
                start = middle + 1
