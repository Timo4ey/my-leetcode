# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:

# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"

# Constraints:

# 1 <= s.length <= 100
# s consists of printable ASCII characters.

# ---------------------------------------Runtime 36 ms Beats 56.10% Memory 16.57 MB Beats 60.20%---------------------------------------


class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        The difference  between upper case letter and lower
        case letter in ASCII is 32
        """
        res = ""
        for char in s:
            code = ord(char)
            code += (65 <= code <= 90) and 32 or 0
            res = f"{res}{chr(code)}"

        return res
