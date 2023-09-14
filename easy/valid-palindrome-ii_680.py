# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

# ---------------------------------------Runtime 100 ms Beats 72.41% Memory 16.8 MB Beats 97.12%---------------------------------------


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                string1 = s[:i] + s[i + 1:]
                string2 = s[:j] + s[j + 1:]
                return string1 == string1[::-1] or string2 == string2[::-1]
            i += 1
            j -= 1
        return True
