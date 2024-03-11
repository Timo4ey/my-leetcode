# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0

# Constraints:

# 0 <= num <= 231 - 1

# Follow up: Could you do it without any loop/recursion in O(1) runtime?


# ---------------------------------------Runtime 36 ms Beats 59.44% Memory 16.50 MB Beats 60.91%---------------------------------------


class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            temp = 0
            for i in num_str:
                temp += int(i)
            num_str = str(temp)

        return int(num_str)
