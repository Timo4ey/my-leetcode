#!/usr/bin/python3
# You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

# The digit sum of n (the sum of its digits).

# The digit product of n (the product of its digits).

# Return true if n is divisible by this sum; otherwise, return false.


# Example 1:

# Input: n = 99

# Output: true

# Explanation:

# Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

# Example 2:

# Input: n = 23

# Output: false

# Explanation:

# Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.


# Constraints:

# 1 <= n <= 106

# ---------------------------------------Runtime 0 ms Beats 100.00% Memory 12.43 MB Beats 47.05%---------------------------------------


class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_n = 0
        product = 1
        temp_n = n

        while temp_n >= 1:
            temp_n, res = divmod(temp_n, 10)
            sum_n += res
            product *= res

        return n % (sum_n + product) == 0


if __name__ == "__main__":
    sol = Solution()
    tests = {
        99: True,
        23: False,
        100: True,
        1: False,
        5: False,
        10: True,
        10525: False,
        16: False,
        20: True,
        26: False,
    }

    for i, a in tests.items():
        r = sol.checkDivisibility(i)
        assert r == a, f"{i=} is not eq {r} it {a}"
