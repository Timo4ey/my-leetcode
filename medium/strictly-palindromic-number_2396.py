# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

# Given an integer n, return true if n is strictly palindromic and false otherwise.

# A string is palindromic if it reads the same forward and backward.


# Example 1:

# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
# Example 2:

# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
# Therefore, we return false.


# ---------------------------------------Runtime 46 ms Beats 59.86% Memory 16.1 MB Beats 92.39%---------------------------------------


# Solution 2
# Time Complexity O(1)
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False


# Solution 1
# Time Complexity O(n)
# ---------------------------------------Runtime 839 ms Beats 5.5% Memory 24 MB Beats 29.37%---------------------------------------


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def get_base(n, base):
            if n == 0:
                return "0"
            nums = []
            while n:
                n, r = divmod(n, base)
                nums.append(str(r))
            return "".join(reversed(nums))

        output = []
        base = 2
        while base <= n:
            output.append(get_base(n, base))
            base += 1
        return all(list(map(lambda x: x == x[::-1], output)))
