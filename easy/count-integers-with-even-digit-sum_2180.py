# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

# The digit sum of a positive integer is the sum of all its digits.


# Example 1:

# Input: num = 4
# Output: 2
# Explanation:
# The only integers less than or equal to 4 whose digit sums are even are 2 and 4.
# Example 2:

# Input: num = 30
# Output: 14
# Explanation:
# The 14 integers less than or equal to 30 whose digit sums are even are
# 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

# ---------------------------------------Runtime 46 ms Beats 64.81% Memory 16.2 MB Beats 82.60%---------------------------------------


from functools import reduce


class Solution:
    def countEven(self, num: int) -> int:
        get_digit_sum = lambda string: reduce(
            lambda acc, number: acc + int(number), string, 0
        )
        counter = 0
        for index in range(1, num + 1):
            counter += int(get_digit_sum(str(index)) % 2 == 0)

        return counter
