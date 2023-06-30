# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


# ---------------------------------------Runtime 55 ms Beats 21.45% Memory 16.1 MB Beats 96.9%---------------------------------------


# Time complexity O(n)
class Solution:
    def reverse(self, x: int) -> int:
        num: int = abs(x)
        negative = 1 if x > 0 else -1
        output: int = 0
        while (num > 0):
            l, r = divmod(num, 10)
            output = output * 10 + r
            num = l
        return output * negative if output.bit_length() <= 31 else 0
