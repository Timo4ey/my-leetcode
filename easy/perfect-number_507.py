# A perfect number is a positive integer that is equal to the sum
# of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

# Example 1:

# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# Example 2:

# Input: num = 7
# Output: false

# ---------------------------------------Runtime 54 ms Beats 53.10% Memory 16.4 MB Beats 25.78%---------------------------------------

import math


# Time Complexity O(logN)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        res = 1
        new_num = int(math.sqrt(num) + 1)
        for count in range(2, new_num):
            if num % count == 0:
                res += count + num // count
            count += 1

        return res == num
