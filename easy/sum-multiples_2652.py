# Code
# Testcase
# Testcase
# Test Result
# 2652. Sum Multiples
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

# Example 1:

# Input: n = 7
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
# Example 2:

# Input: n = 10
# Output: 40
# Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
# Example 3:

# Input: n = 9
# Output: 30
# Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.

# ---------------------------------------Runtime 60 ms Beats 73.34% Memory 16.54 MB Beats 75.18%---------------------------------------


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(
            i
            for i in range(1, n + 1)
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0
        )
