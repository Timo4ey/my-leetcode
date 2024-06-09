# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Example 1:

# Input: s = "abc"

# Output: "abc"

# Explanation:

# There is no digit in the string.

# Example 2:

# Input: s = "cb34"

# Output: ""

# Explanation:

# First, we apply the operation on s[2], and s becomes "c4".

# Then we apply the operation on s[1], and s becomes "".

# Constraints:

# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# The input is generated such that it is possible to delete all digits.

# ---------------------------------------Runtime 55 ms Beats 100.00% Memory 16.51 MB Beats 100.00%---------------------------------------

from collections import deque


class Solution:

    def is_digit(self, item: str) -> bool:
        return item.isdigit()

    def clearDigits(self, s: str) -> str:
        N = len(s)
        if N == 1:
            return s
        # `i` it would be the last vowel
        # `j` it would be the last digit
        i = j = 0

        arr = deque()

        while i <= j <= N - 1:
            if self.is_digit(s[i]):
                i += 1
            if not self.is_digit(s[j]):
                arr.append(s[j])
                i = j
                j += 1
                continue
            if not self.is_digit(s[i]) and self.is_digit(s[j]):
                arr.pop()
                i = i >= 1 and i - 1 or 0
                j += 1

        return "".join(arr)
